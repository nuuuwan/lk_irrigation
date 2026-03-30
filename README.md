# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--30_13:12:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **111,471 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-30 13:12:33 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-30 13:11:49 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-03-30 13:11:11 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-30 13:07:51 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-30 13:07:51 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-30 13:07:15 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-30 13:07:00 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.093 |  |
| 2026-03-30 13:06:38 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 13:06:17 | Glencourse (Kelani Ganga) | 8.29 | 🟢 Normal | -0.038 |  |
| 2026-03-30 13:06:09 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.028 |  |
| 2026-03-30 13:05:35 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-03-30 13:05:34 | Ellagawa (Kalu Ganga) | 3.68 | 🟢 Normal | 0.000 |  |
| 2026-03-30 13:05:30 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.019 |  |
| 2026-03-30 13:05:21 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-30 13:04:54 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.022 |  |
| 2026-03-30 13:04:21 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-30 13:04:12 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | -0.053 |  |
| 2026-03-30 13:03:55 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-30 13:03:39 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-03-30 13:03:23 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-03-30 13:03:15 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 13:03:14 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-03-30 13:03:14 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-30 13:02:37 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-03-30 13:01:53 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-30 13:07:51 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-30 13:02:01 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-03-30 13:03:15 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 13:01:39 | Nawalapitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 13:03:14 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-03-30 13:01:36 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-30 13:07:51 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-30 13:07:15 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-30 13:01:24 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-30 13:11:11 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-30 13:03:04 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-30 13:05:34 | Ellagawa (Kalu Ganga) | 3.68 | 🟢 Normal | 0.000 |  |
| 2026-03-30 13:00:15 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-30 13:03:55 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-30 13:03:39 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-03-30 13:05:21 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-30 13:12:33 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-30 13:03:01 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-30 13:02:59 | Badalgama (Maha Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-03-30 13:06:38 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 13:00:45 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-30 13:02:19 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 13:05:35 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-03-30 13:04:21 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-30 13:11:49 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-03-30 13:03:14 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-03-30 13:05:30 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.019 |  |
| 2026-03-30 13:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-03-30 13:02:20 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-03-30 13:03:23 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-03-30 13:01:24 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-03-30 13:04:54 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.022 |  |
| 2026-03-30 13:06:09 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.028 |  |
| 2026-03-30 13:06:17 | Glencourse (Kelani Ganga) | 8.29 | 🟢 Normal | -0.038 |  |
| 2026-03-30 13:04:12 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | -0.053 |  |
| 2026-03-30 13:07:00 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.093 |  |
| 2026-03-30 13:00:54 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.234 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)