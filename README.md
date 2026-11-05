# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--05_17:03:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **307,664 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 17:03:16 | Giriulla (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-11-05 17:03:13 | Manampitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-05 17:03:05 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 17:03:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.98 | 🟢 Normal | -0.060 |  |
| 2026-11-05 17:02:52 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-11-05 17:02:28 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.005 |  |
| 2026-11-05 17:02:25 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-05 17:02:13 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-05 17:01:53 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-11-05 17:01:24 | Wellawaya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.030 |  |
| 2026-11-05 17:01:21 | Thanamalwila (Kirindi Oya) | 1.90 | 🟢 Normal | -0.081 |  |
| 2026-11-05 17:00:47 | Thanthirimale (Malwathu Oya) | 1.85 | 🟢 Normal | -0.020 |  |
| 2026-11-05 17:00:44 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | 0.000 |  |
| 2026-11-05 17:00:41 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-05 16:55:46 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | 0.000 |  |
| 2026-11-05 16:23:40 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | -0.007 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 16:05:21 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 76.596 | 🔺 Rising |
| 2026-11-05 17:03:13 | Manampitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-05 15:01:23 | Ellagawa (Kalu Ganga) | 6.56 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-05 16:05:54 | Thawalama (Gin Ganga) | 2.12 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-05 16:08:12 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-11-05 17:02:25 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-05 17:03:05 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 16:12:38 | Thalgahagoda (Nilwala Ganga) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 17:00:44 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | 0.000 |  |
| 2026-11-05 17:02:13 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-05 17:03:16 | Giriulla (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-11-05 16:04:35 | Galgamuwa (Mee Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-05 16:11:44 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-05 17:00:41 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-05 16:02:57 | Putupaula (Kalu Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-11-05 17:02:28 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.005 |  |
| 2026-11-05 16:23:40 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | -0.007 |  |
| 2026-11-05 16:16:34 | Magura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.009 |  |
| 2026-11-05 17:01:53 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-11-05 17:02:52 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-11-05 16:04:23 | Peradeniya (Mahaweli Ganga) | 2.47 | 🟢 Normal | -0.010 |  |
| 2026-11-05 16:03:26 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-11-05 16:14:53 | Urawa (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.018 |  |
| 2026-11-05 16:05:40 | Kuda Oya (Kirindi Oya) | 2.23 | 🟢 Normal | -0.019 |  |
| 2026-11-05 15:11:39 | Pitabeddara (Nilwala Ganga) | 1.44 | 🟢 Normal | -0.019 |  |
| 2026-11-05 16:05:48 | Badalgama (Maha Oya) | 3.25 | 🟢 Normal | -0.020 |  |
| 2026-11-05 17:00:47 | Thanthirimale (Malwathu Oya) | 1.85 | 🟢 Normal | -0.020 |  |
| 2026-11-05 16:05:13 | Moragaswewa (Deduru Oya) | 3.38 | 🟢 Normal | -0.029 |  |
| 2026-11-05 17:01:24 | Wellawaya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.030 |  |
| 2026-11-05 16:01:56 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | -0.031 |  |
| 2026-11-05 16:07:57 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.037 |  |
| 2026-11-05 16:03:00 | Hanwella (Kelani Ganga) | 2.52 | 🟢 Normal | -0.040 |  |
| 2026-11-05 16:09:05 | Panadugama (Nilwala Ganga) | 4.34 | 🟢 Normal | -0.048 |  |
| 2026-11-05 16:13:04 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | -0.052 |  |
| 2026-11-05 16:08:38 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.057 |  |
| 2026-11-05 17:03:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.98 | 🟢 Normal | -0.060 |  |
| 2026-11-05 16:05:19 | Glencourse (Kelani Ganga) | 10.32 | 🟢 Normal | -0.079 |  |
| 2026-11-05 17:01:21 | Thanamalwila (Kirindi Oya) | 1.90 | 🟢 Normal | -0.081 |  |
| 2026-11-05 16:02:35 | Rathnapura (Kalu Ganga) | 3.05 | 🟢 Normal | -0.140 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)