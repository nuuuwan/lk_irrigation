# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--17_10:08:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **290,264 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 10:08:09 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.061 |  |
| 2026-10-17 10:07:34 | Baddegama (Gin Ganga) | 3.38 | 🟢 Normal | 0.000 |  |
| 2026-10-17 10:06:05 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.062 |  |
| 2026-10-17 10:05:16 | Galgamuwa (Mee Oya) | 1.71 | 🟢 Normal | -0.011 |  |
| 2026-10-17 10:04:50 | Putupaula (Kalu Ganga) | 2.18 | 🟢 Normal | -0.019 |  |
| 2026-10-17 10:04:39 | Urawa (Nilwala Ganga) | 1.29 | 🟢 Normal | -0.040 |  |
| 2026-10-17 10:03:55 | Moraketiya (Walawe Ganga) | 1.43 | 🟢 Normal | -0.029 |  |
| 2026-10-17 10:03:50 | Badalgama (Maha Oya) | 3.31 | 🟢 Normal | -0.042 |  |
| 2026-10-17 10:03:35 | Thalgahagoda (Nilwala Ganga) | 2.01 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-10-17 10:03:34 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-17 10:03:21 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-10-17 10:03:13 | Hanwella (Kelani Ganga) | 3.69 | 🟢 Normal | -0.060 |  |
| 2026-10-17 10:03:05 | Thanamalwila (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-17 10:02:55 | Giriulla (Maha Oya) | 1.98 | 🟢 Normal | -0.050 |  |
| 2026-10-17 10:02:50 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-10-17 10:02:38 | Ellagawa (Kalu Ganga) | 7.61 | 🟢 Normal | -0.010 |  |
| 2026-10-17 10:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.77 | 🟡 Alert | -0.020 |  |
| 2026-10-17 10:02:17 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-17 10:02:14 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-10-17 10:02:09 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-17 10:02:06 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-17 10:02:06 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-17 10:02:05 | Moragaswewa (Deduru Oya) | 1.48 | 🟢 Normal | -0.079 |  |
| 2026-10-17 10:01:44 | Dunamale (Aththanagalu Oya) | 3.14 | 🟢 Normal | -0.042 |  |
| 2026-10-17 10:01:31 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | -0.050 |  |
| 2026-10-17 10:01:22 | Glencourse (Kelani Ganga) | 11.30 | 🟢 Normal | -0.097 |  |
| 2026-10-17 10:01:13 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | -0.040 |  |
| 2026-10-17 10:00:49 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-17 10:00:40 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-10-17 10:00:31 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 09:17:13 | Panadugama (Nilwala Ganga) | 6.26 | 🟠 Minor Flood | 0.017 | 🔺 Rising |
| 2026-10-17 10:03:35 | Thalgahagoda (Nilwala Ganga) | 2.01 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-10-17 10:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.77 | 🟡 Alert | -0.020 |  |
| 2026-10-17 09:01:41 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-10-17 09:00:51 | Thanthirimale (Malwathu Oya) | 2.47 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-10-17 10:02:09 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-17 10:00:31 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 10:02:06 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-17 10:07:34 | Baddegama (Gin Ganga) | 3.38 | 🟢 Normal | 0.000 |  |
| 2026-10-17 10:02:06 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-17 10:00:49 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-17 10:02:17 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-17 10:03:34 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-17 10:00:40 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-10-17 10:03:21 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-10-17 10:03:05 | Thanamalwila (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-17 10:02:14 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-10-17 10:02:38 | Ellagawa (Kalu Ganga) | 7.61 | 🟢 Normal | -0.010 |  |
| 2026-10-17 10:02:50 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-10-17 10:05:16 | Galgamuwa (Mee Oya) | 1.71 | 🟢 Normal | -0.011 |  |
| 2026-10-17 10:04:50 | Putupaula (Kalu Ganga) | 2.18 | 🟢 Normal | -0.019 |  |
| 2026-10-17 09:02:08 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-10-17 09:05:40 | Holombuwa (Kelani Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-10-17 09:04:10 | Pitabeddara (Nilwala Ganga) | 2.19 | 🟢 Normal | -0.022 |  |
| 2026-10-17 10:03:55 | Moraketiya (Walawe Ganga) | 1.43 | 🟢 Normal | -0.029 |  |
| 2026-10-17 10:01:13 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | -0.040 |  |
| 2026-10-17 10:04:39 | Urawa (Nilwala Ganga) | 1.29 | 🟢 Normal | -0.040 |  |
| 2026-10-17 10:03:50 | Badalgama (Maha Oya) | 3.31 | 🟢 Normal | -0.042 |  |
| 2026-10-17 10:01:44 | Dunamale (Aththanagalu Oya) | 3.14 | 🟢 Normal | -0.042 |  |
| 2026-10-17 09:04:46 | Thawalama (Gin Ganga) | 2.94 | 🟢 Normal | -0.044 |  |
| 2026-10-17 10:02:55 | Giriulla (Maha Oya) | 1.98 | 🟢 Normal | -0.050 |  |
| 2026-10-17 10:01:31 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | -0.050 |  |
| 2026-10-17 10:03:13 | Hanwella (Kelani Ganga) | 3.69 | 🟢 Normal | -0.060 |  |
| 2026-10-17 10:08:09 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.061 |  |
| 2026-10-17 10:06:05 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.062 |  |
| 2026-10-17 09:16:36 | Magura (Kalu Ganga) | 3.55 | 🟢 Normal | -0.074 |  |
| 2026-10-17 10:02:05 | Moragaswewa (Deduru Oya) | 1.48 | 🟢 Normal | -0.079 |  |
| 2026-10-17 10:01:22 | Glencourse (Kelani Ganga) | 11.30 | 🟢 Normal | -0.097 |  |
| 2026-10-17 09:04:55 | Rathnapura (Kalu Ganga) | 3.36 | 🟢 Normal | -0.118 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)