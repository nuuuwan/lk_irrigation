# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--31_15:13:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **303,084 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 15:13:12 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.035 |  |
| 2026-10-31 15:12:54 | Baddegama (Gin Ganga) | 2.46 | 🟢 Normal | -0.029 |  |
| 2026-10-31 15:10:54 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | -0.035 |  |
| 2026-10-31 15:08:37 | Thalgahagoda (Nilwala Ganga) | 1.61 | 🟡 Alert | -0.009 |  |
| 2026-10-31 15:07:04 | Putupaula (Kalu Ganga) | 2.00 | 🟢 Normal | -0.102 |  |
| 2026-10-31 15:06:43 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | -0.019 |  |
| 2026-10-31 15:06:22 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-31 15:06:21 | Urawa (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.012 |  |
| 2026-10-31 15:05:56 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.030 |  |
| 2026-10-31 15:05:24 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.019 |  |
| 2026-10-31 15:05:10 | Panadugama (Nilwala Ganga) | 4.63 | 🟢 Normal | -0.033 |  |
| 2026-10-31 15:05:04 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-31 15:05:01 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-10-31 15:04:40 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-31 15:04:00 | Galgamuwa (Mee Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-10-31 15:03:57 | Glencourse (Kelani Ganga) | 10.54 | 🟢 Normal | -0.063 |  |
| 2026-10-31 15:03:38 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-10-31 15:03:13 | Magura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.020 |  |
| 2026-10-31 15:02:57 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-10-31 15:02:53 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-10-31 15:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.70 | 🟢 Normal | -0.111 |  |
| 2026-10-31 15:02:31 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | -0.080 |  |
| 2026-10-31 15:02:30 | Hanwella (Kelani Ganga) | 2.57 | 🟢 Normal | -0.020 |  |
| 2026-10-31 15:02:29 | Dunamale (Aththanagalu Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-10-31 15:02:20 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | -0.040 |  |
| 2026-10-31 15:02:19 | Badalgama (Maha Oya) | 2.91 | 🟢 Normal | -0.020 |  |
| 2026-10-31 15:02:04 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-10-31 15:02:02 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-31 15:01:49 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-31 15:01:29 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-10-31 15:01:24 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 15:01:15 | Pitabeddara (Nilwala Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-10-31 15:01:14 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-10-31 15:01:07 | Peradeniya (Mahaweli Ganga) | 2.69 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-31 15:01:03 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.109 |  |
| 2026-10-31 15:00:56 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-31 15:00:30 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.040 |  |
| 2026-10-31 15:00:21 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | -0.023 |  |
| 2026-10-31 15:00:14 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 15:08:37 | Thalgahagoda (Nilwala Ganga) | 1.61 | 🟡 Alert | -0.009 |  |
| 2026-10-31 15:04:40 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-31 15:05:01 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-10-31 15:01:07 | Peradeniya (Mahaweli Ganga) | 2.69 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-31 15:00:56 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-31 15:06:22 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-31 15:02:04 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-10-31 15:00:14 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-10-31 15:02:02 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-31 15:01:24 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 15:01:49 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-31 15:05:04 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-31 15:03:38 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-10-31 15:02:29 | Dunamale (Aththanagalu Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-10-31 15:01:29 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-10-31 15:02:53 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-10-31 15:01:14 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-10-31 15:02:57 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-10-31 15:01:15 | Pitabeddara (Nilwala Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-10-31 15:04:00 | Galgamuwa (Mee Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-10-31 15:06:21 | Urawa (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.012 |  |
| 2026-10-31 15:06:43 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | -0.019 |  |
| 2026-10-31 15:05:24 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.019 |  |
| 2026-10-31 15:03:13 | Magura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.020 |  |
| 2026-10-31 15:02:19 | Badalgama (Maha Oya) | 2.91 | 🟢 Normal | -0.020 |  |
| 2026-10-31 15:02:30 | Hanwella (Kelani Ganga) | 2.57 | 🟢 Normal | -0.020 |  |
| 2026-10-31 15:00:21 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | -0.023 |  |
| 2026-10-31 15:12:54 | Baddegama (Gin Ganga) | 2.46 | 🟢 Normal | -0.029 |  |
| 2026-10-31 15:05:56 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.030 |  |
| 2026-10-31 15:05:10 | Panadugama (Nilwala Ganga) | 4.63 | 🟢 Normal | -0.033 |  |
| 2026-10-31 15:10:54 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | -0.035 |  |
| 2026-10-31 15:13:12 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.035 |  |
| 2026-10-31 15:00:30 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.040 |  |
| 2026-10-31 15:02:20 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | -0.040 |  |
| 2026-10-31 15:03:57 | Glencourse (Kelani Ganga) | 10.54 | 🟢 Normal | -0.063 |  |
| 2026-10-31 15:02:31 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | -0.080 |  |
| 2026-10-31 15:07:04 | Putupaula (Kalu Ganga) | 2.00 | 🟢 Normal | -0.102 |  |
| 2026-10-31 15:01:03 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.109 |  |
| 2026-10-31 15:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.70 | 🟢 Normal | -0.111 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)