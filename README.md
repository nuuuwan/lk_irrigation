# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--19_07:18:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **291,956 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 07:18:26 | Pitabeddara (Nilwala Ganga) | 2.05 | 🟢 Normal | -0.081 |  |
| 2026-10-19 07:13:18 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-19 07:10:37 | Baddegama (Gin Ganga) | 2.69 | 🟢 Normal | -0.037 |  |
| 2026-10-19 07:10:33 | Panadugama (Nilwala Ganga) | 5.49 | 🟡 Alert | -0.082 |  |
| 2026-10-19 07:10:11 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.009 |  |
| 2026-10-19 07:08:51 | Rathnapura (Kalu Ganga) | 3.53 | 🟢 Normal | -0.146 |  |
| 2026-10-19 07:07:47 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | -0.018 |  |
| 2026-10-19 07:07:39 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | -0.013 |  |
| 2026-10-19 07:07:23 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | -0.019 |  |
| 2026-10-19 07:07:07 | Glencourse (Kelani Ganga) | 11.39 | 🟢 Normal | -0.100 |  |
| 2026-10-19 07:05:18 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.029 |  |
| 2026-10-19 07:04:55 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-19 07:04:48 | Dunamale (Aththanagalu Oya) | 2.09 | 🟢 Normal | -0.010 |  |
| 2026-10-19 07:04:18 | Hanwella (Kelani Ganga) | 3.61 | 🟢 Normal | -0.077 |  |
| 2026-10-19 07:03:30 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-19 07:03:27 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 07:03:25 | Norwood (Kelani Ganga) | 1.31 | 🟢 Normal | -0.056 |  |
| 2026-10-19 07:03:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.92 | 🟢 Normal | -0.213 |  |
| 2026-10-19 07:03:10 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-10-19 07:03:05 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-19 07:03:04 | Giriulla (Maha Oya) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 07:02:51 | Ellagawa (Kalu Ganga) | 7.32 | 🟢 Normal | -0.021 |  |
| 2026-10-19 07:02:18 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-19 07:02:15 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-19 07:02:13 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-19 07:02:07 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-10-19 07:02:05 | Thawalama (Gin Ganga) | 2.44 | 🟢 Normal | -0.031 |  |
| 2026-10-19 07:02:00 | Putupaula (Kalu Ganga) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-10-19 07:01:52 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.031 |  |
| 2026-10-19 07:01:49 | Manampitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-10-19 07:01:34 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.097 |  |
| 2026-10-19 07:01:34 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.042 |  |
| 2026-10-19 07:01:29 | Moragaswewa (Deduru Oya) | 1.90 | 🟢 Normal | -0.106 |  |
| 2026-10-19 07:01:10 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-19 07:01:07 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-19 07:00:56 | Moraketiya (Walawe Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-19 07:00:25 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | -0.072 |  |
| 2026-10-19 07:00:11 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.063 |  |
| 2026-10-19 06:39:13 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-19 06:39:01 | Urawa (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 06:05:12 | Thalgahagoda (Nilwala Ganga) | 1.95 | 🟠 Minor Flood | -0.034 |  |
| 2026-10-19 07:10:33 | Panadugama (Nilwala Ganga) | 5.49 | 🟡 Alert | -0.082 |  |
| 2026-10-19 07:04:55 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-19 07:03:27 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 07:03:04 | Giriulla (Maha Oya) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 07:01:10 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-19 07:02:18 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-19 07:13:18 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-19 07:00:56 | Moraketiya (Walawe Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-19 07:02:15 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-19 07:03:30 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-19 06:39:01 | Urawa (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-19 07:10:11 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.009 |  |
| 2026-10-19 07:04:48 | Dunamale (Aththanagalu Oya) | 2.09 | 🟢 Normal | -0.010 |  |
| 2026-10-19 07:03:10 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-10-19 07:02:13 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-19 07:02:07 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-10-19 07:01:49 | Manampitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-10-19 07:07:39 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | -0.013 |  |
| 2026-10-19 07:07:47 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | -0.018 |  |
| 2026-10-19 07:07:23 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | -0.019 |  |
| 2026-10-19 07:02:00 | Putupaula (Kalu Ganga) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-10-19 06:03:01 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.021 |  |
| 2026-10-19 07:02:51 | Ellagawa (Kalu Ganga) | 7.32 | 🟢 Normal | -0.021 |  |
| 2026-10-19 07:05:18 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.029 |  |
| 2026-10-19 07:01:52 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.031 |  |
| 2026-10-19 07:02:05 | Thawalama (Gin Ganga) | 2.44 | 🟢 Normal | -0.031 |  |
| 2026-10-19 07:10:37 | Baddegama (Gin Ganga) | 2.69 | 🟢 Normal | -0.037 |  |
| 2026-10-19 07:01:34 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.042 |  |
| 2026-10-19 07:03:25 | Norwood (Kelani Ganga) | 1.31 | 🟢 Normal | -0.056 |  |
| 2026-10-19 07:00:11 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.063 |  |
| 2026-10-19 07:00:25 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | -0.072 |  |
| 2026-10-19 07:04:18 | Hanwella (Kelani Ganga) | 3.61 | 🟢 Normal | -0.077 |  |
| 2026-10-19 07:18:26 | Pitabeddara (Nilwala Ganga) | 2.05 | 🟢 Normal | -0.081 |  |
| 2026-10-19 07:01:34 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.097 |  |
| 2026-10-19 07:07:07 | Glencourse (Kelani Ganga) | 11.39 | 🟢 Normal | -0.100 |  |
| 2026-10-19 07:01:29 | Moragaswewa (Deduru Oya) | 1.90 | 🟢 Normal | -0.106 |  |
| 2026-10-19 07:08:51 | Rathnapura (Kalu Ganga) | 3.53 | 🟢 Normal | -0.146 |  |
| 2026-10-19 07:03:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.92 | 🟢 Normal | -0.213 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)