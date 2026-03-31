# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--31_13:13:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **112,356 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-31 13:13:59 | Panadugama (Nilwala Ganga) | 1.85 | 🟢 Normal | -0.009 |  |
| 2026-03-31 13:13:48 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | -0.009 |  |
| 2026-03-31 13:11:22 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:09:38 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-31 13:08:20 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:07:55 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-03-31 13:07:34 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | -0.028 |  |
| 2026-03-31 13:06:49 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:06:39 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.009 |  |
| 2026-03-31 13:06:38 | Baddegama (Gin Ganga) | 0.71 | 🟢 Normal | 5.538 | 🔺 Rising |
| 2026-03-31 13:06:16 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.009 |  |
| 2026-03-31 13:06:12 | Baddegama (Gin Ganga) | 0.67 | 🟢 Normal | 5.538 | 🔺 Rising |
| 2026-03-31 13:05:02 | Ellagawa (Kalu Ganga) | 3.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 13:04:41 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:04:08 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:04:05 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:03:59 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 13:03:58 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:03:55 | Rathnapura (Kalu Ganga) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-03-31 13:03:45 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:03:32 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:03:10 | Badalgama (Maha Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:03:08 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:03:01 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:02:44 | Deraniyagala (Kelani Ganga) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-03-31 13:02:36 | Weraganthota (Mahaweli Ganga) | -2.46 | 🟢 Normal | -0.253 |  |
| 2026-03-31 13:02:33 | Nawalapitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 13:02:33 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:02:23 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:02:19 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:02:17 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-03-31 13:02:15 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.049 |  |
| 2026-03-31 13:02:11 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-03-31 13:01:51 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:01:45 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:01:25 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:01:24 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:01:14 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:01:13 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-31 13:06:38 | Baddegama (Gin Ganga) | 0.71 | 🟢 Normal | 5.538 | 🔺 Rising |
| 2026-03-31 13:02:17 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-03-31 13:07:55 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-03-31 13:09:38 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-31 13:05:02 | Ellagawa (Kalu Ganga) | 3.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 13:02:33 | Nawalapitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 13:03:59 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 13:11:22 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:08:20 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:03:08 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:04:05 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:01:45 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:01:24 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:03:01 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:03:45 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:01:59 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:02:33 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:01:13 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:01:25 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:02:21 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:02:19 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:03:58 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:02:11 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:03:10 | Badalgama (Maha Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:04:41 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:01:14 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:06:49 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:04:08 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:02:23 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 13:13:48 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | -0.009 |  |
| 2026-03-31 13:13:59 | Panadugama (Nilwala Ganga) | 1.85 | 🟢 Normal | -0.009 |  |
| 2026-03-31 13:06:39 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.009 |  |
| 2026-03-31 13:06:16 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.009 |  |
| 2026-03-31 13:02:44 | Deraniyagala (Kelani Ganga) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-03-31 13:03:55 | Rathnapura (Kalu Ganga) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-03-31 13:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-03-31 13:07:34 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | -0.028 |  |
| 2026-03-31 13:02:15 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.049 |  |
| 2026-03-31 13:02:36 | Weraganthota (Mahaweli Ganga) | -2.46 | 🟢 Normal | -0.253 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)