# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--31_08:19:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **302,811 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 08:19:04 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-31 08:13:34 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-10-31 08:12:51 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.126 |  |
| 2026-10-31 08:08:37 | Baddegama (Gin Ganga) | 2.71 | 🟢 Normal | -0.040 |  |
| 2026-10-31 08:07:59 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | -0.009 |  |
| 2026-10-31 08:07:21 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.088 |  |
| 2026-10-31 08:06:25 | Glencourse (Kelani Ganga) | 10.64 | 🟢 Normal | 0.000 |  |
| 2026-10-31 08:06:15 | Urawa (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.012 |  |
| 2026-10-31 08:05:53 | Rathnapura (Kalu Ganga) | 2.33 | 🟢 Normal | -0.019 |  |
| 2026-10-31 08:05:11 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-31 08:05:04 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-10-31 08:04:30 | Putupaula (Kalu Ganga) | 2.57 | 🟢 Normal | -0.054 |  |
| 2026-10-31 08:04:27 | Badalgama (Maha Oya) | 3.09 | 🟢 Normal | 0.000 |  |
| 2026-10-31 08:04:24 | Magura (Kalu Ganga) | 2.39 | 🟢 Normal | -0.103 |  |
| 2026-10-31 08:04:18 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | -0.039 |  |
| 2026-10-31 08:04:10 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-10-31 08:04:05 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | -0.020 |  |
| 2026-10-31 08:03:51 | Giriulla (Maha Oya) | 1.75 | 🟢 Normal | -0.049 |  |
| 2026-10-31 08:03:44 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.020 |  |
| 2026-10-31 08:03:43 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-10-31 08:03:42 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 08:03:34 | Galgamuwa (Mee Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-10-31 08:03:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.31 | 🟡 Alert | -0.090 |  |
| 2026-10-31 08:03:31 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-10-31 08:03:26 | Hanwella (Kelani Ganga) | 2.70 | 🟢 Normal | -0.030 |  |
| 2026-10-31 08:03:15 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.034 |  |
| 2026-10-31 08:03:03 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-31 08:02:31 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-31 08:02:21 | Ellagawa (Kalu Ganga) | 7.00 | 🟢 Normal | -0.060 |  |
| 2026-10-31 08:02:04 | Panadugama (Nilwala Ganga) | 4.84 | 🟢 Normal | -0.040 |  |
| 2026-10-31 08:01:55 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | -0.040 |  |
| 2026-10-31 08:01:45 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-31 08:01:43 | Moragaswewa (Deduru Oya) | 1.07 | 🟢 Normal | -0.066 |  |
| 2026-10-31 08:01:37 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.030 |  |
| 2026-10-31 08:01:30 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-31 08:00:54 | Thalgahagoda (Nilwala Ganga) | 1.68 | 🟡 Alert | 0.000 |  |
| 2026-10-31 08:00:50 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-31 08:00:23 | Pitabeddara (Nilwala Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-10-31 08:00:15 | Weraganthota (Mahaweli Ganga) | -2.99 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 08:00:54 | Thalgahagoda (Nilwala Ganga) | 1.68 | 🟡 Alert | 0.000 |  |
| 2026-10-31 08:03:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.31 | 🟡 Alert | -0.090 |  |
| 2026-10-31 08:04:10 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-10-31 08:19:04 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-31 08:01:45 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-31 08:00:50 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-31 08:01:30 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-31 08:03:42 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 08:00:23 | Pitabeddara (Nilwala Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-10-31 08:03:03 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-31 08:02:31 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-31 08:06:25 | Glencourse (Kelani Ganga) | 10.64 | 🟢 Normal | 0.000 |  |
| 2026-10-31 08:04:27 | Badalgama (Maha Oya) | 3.09 | 🟢 Normal | 0.000 |  |
| 2026-10-31 08:05:11 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-31 08:03:43 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-10-31 08:13:34 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-10-31 08:07:59 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | -0.009 |  |
| 2026-10-31 08:05:04 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-10-31 08:03:34 | Galgamuwa (Mee Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-10-31 08:06:15 | Urawa (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.012 |  |
| 2026-10-31 08:05:53 | Rathnapura (Kalu Ganga) | 2.33 | 🟢 Normal | -0.019 |  |
| 2026-10-31 08:03:31 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-10-31 08:04:05 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | -0.020 |  |
| 2026-10-31 08:03:44 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.020 |  |
| 2026-10-31 08:01:37 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.030 |  |
| 2026-10-31 08:00:15 | Weraganthota (Mahaweli Ganga) | -2.99 | 🟢 Normal | -0.030 |  |
| 2026-10-31 08:03:26 | Hanwella (Kelani Ganga) | 2.70 | 🟢 Normal | -0.030 |  |
| 2026-10-31 08:03:15 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.034 |  |
| 2026-10-31 08:04:18 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | -0.039 |  |
| 2026-10-31 08:02:04 | Panadugama (Nilwala Ganga) | 4.84 | 🟢 Normal | -0.040 |  |
| 2026-10-31 08:08:37 | Baddegama (Gin Ganga) | 2.71 | 🟢 Normal | -0.040 |  |
| 2026-10-31 08:01:55 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | -0.040 |  |
| 2026-10-31 08:03:51 | Giriulla (Maha Oya) | 1.75 | 🟢 Normal | -0.049 |  |
| 2026-10-31 08:04:30 | Putupaula (Kalu Ganga) | 2.57 | 🟢 Normal | -0.054 |  |
| 2026-10-31 08:02:21 | Ellagawa (Kalu Ganga) | 7.00 | 🟢 Normal | -0.060 |  |
| 2026-10-31 08:01:43 | Moragaswewa (Deduru Oya) | 1.07 | 🟢 Normal | -0.066 |  |
| 2026-10-31 08:07:21 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.088 |  |
| 2026-10-31 08:04:24 | Magura (Kalu Ganga) | 2.39 | 🟢 Normal | -0.103 |  |
| 2026-10-31 08:12:51 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.126 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)