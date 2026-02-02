# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--02_21:11:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **62,780 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-02 21:11:12 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-02 21:11:09 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-02 21:08:50 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | -0.010 |  |
| 2026-02-02 21:08:43 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | -0.018 |  |
| 2026-02-02 21:07:35 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | -0.019 |  |
| 2026-02-02 21:07:23 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-02-02 21:06:34 | Padiyathalawa (Maduru Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-02 21:06:29 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-02 21:06:28 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-02-02 21:06:10 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.096 |  |
| 2026-02-02 21:05:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.049 |  |
| 2026-02-02 21:05:34 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-02 21:05:15 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-02 21:05:04 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-02 21:04:38 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 21:04:16 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-02 21:04:10 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-02 21:04:10 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-02 21:03:37 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-02 21:03:32 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-02-02 21:03:30 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-02 21:03:12 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-02-02 21:02:58 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-02 21:02:41 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.011 |  |
| 2026-02-02 21:02:26 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 21:02:21 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 21:02:03 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.080 |  |
| 2026-02-02 21:02:02 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-02-02 21:01:51 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-02-02 21:01:51 | Yaka Wewa (Ma Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-02-02 21:01:48 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-02 21:01:41 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-02 21:01:12 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.083 |  |
| 2026-02-02 21:01:12 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-02 21:00:54 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-02 21:00:31 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-02 21:07:23 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-02-02 21:01:51 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-02-02 21:06:28 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-02-02 21:04:10 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-02 21:03:32 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-02-02 21:05:04 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-02 21:03:30 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-02 21:11:12 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-02 21:04:38 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 21:02:21 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 21:01:48 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-02 21:02:58 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-02 21:01:51 | Yaka Wewa (Ma Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-02-02 21:01:41 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-02 21:11:09 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:09:57 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-02 21:04:10 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-02 21:06:34 | Padiyathalawa (Maduru Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-02 21:03:37 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-02 21:05:15 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-02 21:00:54 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-02 21:06:29 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-02 21:02:26 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 21:05:34 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-02 21:04:16 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-02 21:00:31 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-02 21:01:12 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-02 21:08:50 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | -0.010 |  |
| 2026-02-02 21:02:02 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-02-02 21:02:41 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.011 |  |
| 2026-02-02 21:08:43 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | -0.018 |  |
| 2026-02-02 21:07:35 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | -0.019 |  |
| 2026-02-02 21:03:12 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-02-02 18:03:26 | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.021 |  |
| 2026-02-02 21:05:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.049 |  |
| 2026-02-02 18:01:17 | Weraganthota (Mahaweli Ganga) | -2.52 | 🟢 Normal | -0.061 |  |
| 2026-02-02 21:02:03 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.080 |  |
| 2026-02-02 21:01:12 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.083 |  |
| 2026-02-02 21:06:10 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)