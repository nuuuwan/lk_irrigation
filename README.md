# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--15_21:10:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **98,346 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 21:10:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | -0.019 |  |
| 2026-03-15 21:10:36 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-15 21:08:33 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 21:08:31 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.009 |  |
| 2026-03-15 21:08:19 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-15 21:08:19 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | -0.018 |  |
| 2026-03-15 21:07:16 | Glencourse (Kelani Ganga) | 8.73 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-15 21:06:54 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | 0.000 |  |
| 2026-03-15 21:06:44 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.032 |  |
| 2026-03-15 21:06:23 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.032 |  |
| 2026-03-15 21:06:15 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | -0.096 |  |
| 2026-03-15 21:06:00 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-15 21:05:05 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-03-15 21:04:28 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 21:04:28 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-03-15 21:03:56 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-15 21:03:51 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-03-15 21:03:46 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-15 21:03:31 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 21:03:22 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-15 21:03:20 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-15 21:03:17 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-15 21:03:14 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-15 21:03:04 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-15 21:02:36 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | -0.021 |  |
| 2026-03-15 21:02:33 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-15 21:02:22 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-03-15 21:02:20 | Thaldena (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.495 | 🔺 Rising |
| 2026-03-15 21:02:20 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-03-15 21:02:19 | Manampitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.058 |  |
| 2026-03-15 21:02:12 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | -0.022 |  |
| 2026-03-15 21:02:09 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-03-15 21:02:09 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-03-15 21:01:50 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-03-15 21:01:50 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-15 21:01:02 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 21:00:54 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 21:02:20 | Thaldena (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.495 | 🔺 Rising |
| 2026-03-15 21:02:22 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-03-15 21:05:05 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-03-15 21:01:50 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-03-15 21:07:16 | Glencourse (Kelani Ganga) | 8.73 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-15 21:03:17 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-15 21:01:50 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-15 21:04:28 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 21:00:54 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-15 21:03:14 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-15 21:01:02 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 21:03:31 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:05:04 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-15 21:03:22 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-15 21:03:20 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-15 21:06:54 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | 0.000 |  |
| 2026-03-15 21:06:00 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-15 21:10:36 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-15 21:08:19 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-15 21:03:56 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-15 21:03:46 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-15 21:08:33 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:02:20 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-15 21:03:04 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-15 21:08:31 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.009 |  |
| 2026-03-15 21:02:09 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-03-15 21:03:51 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-03-15 21:02:09 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-03-15 21:04:28 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-03-15 21:08:19 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | -0.018 |  |
| 2026-03-15 21:10:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | -0.019 |  |
| 2026-03-15 21:02:20 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-03-15 21:02:36 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | -0.021 |  |
| 2026-03-15 21:02:12 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | -0.022 |  |
| 2026-03-15 21:06:23 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.032 |  |
| 2026-03-15 21:06:44 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.032 |  |
| 2026-03-15 18:02:59 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.040 |  |
| 2026-03-15 21:02:19 | Manampitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.058 |  |
| 2026-03-15 21:06:15 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)