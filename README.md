# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--03_16:03:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **305,825 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 16:03:22 | Wellawaya (Kirindi Oya) | 1.95 | 🟢 Normal | 0.306 | 🔺 Rising |
| 2026-11-03 16:03:16 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.011 |  |
| 2026-11-03 16:03:10 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-03 16:03:04 | Norwood (Kelani Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-03 16:02:51 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-03 16:02:22 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.040 |  |
| 2026-11-03 16:02:06 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-03 16:01:59 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-03 16:01:40 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | -0.112 |  |
| 2026-11-03 16:01:28 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-11-03 16:01:16 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 16:01:03 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-03 16:00:58 | Moragaswewa (Deduru Oya) | 4.27 | 🟢 Normal | -0.023 |  |
| 2026-11-03 16:00:33 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 16:03:22 | Wellawaya (Kirindi Oya) | 1.95 | 🟢 Normal | 0.306 | 🔺 Rising |
| 2026-11-03 15:02:40 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-11-03 15:09:04 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-03 16:02:06 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-03 16:03:10 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-03 16:02:51 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-03 15:08:36 | Baddegama (Gin Ganga) | 2.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-03 15:00:12 | Horowpothana (Yan Oya) | 2.61 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-03 16:01:16 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 16:03:04 | Norwood (Kelani Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-03 16:01:03 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-03 15:07:06 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-03 16:01:59 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-03 14:03:59 | Urawa (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-03 16:00:33 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-03 15:01:24 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-11-03 15:06:09 | Pitabeddara (Nilwala Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-11-03 16:01:28 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-11-03 16:03:16 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.011 |  |
| 2026-11-03 15:06:32 | Magura (Kalu Ganga) | 2.05 | 🟢 Normal | -0.012 |  |
| 2026-11-03 15:01:48 | Thanamalwila (Kirindi Oya) | 1.75 | 🟢 Normal | -0.020 |  |
| 2026-11-03 15:04:03 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | -0.020 |  |
| 2026-11-03 15:02:16 | Putupaula (Kalu Ganga) | 1.16 | 🟢 Normal | -0.021 |  |
| 2026-11-03 15:02:40 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.021 |  |
| 2026-11-03 15:01:45 | Panadugama (Nilwala Ganga) | 3.86 | 🟢 Normal | -0.021 |  |
| 2026-11-03 15:02:39 | Galgamuwa (Mee Oya) | 0.83 | 🟢 Normal | -0.022 |  |
| 2026-11-03 16:00:58 | Moragaswewa (Deduru Oya) | 4.27 | 🟢 Normal | -0.023 |  |
| 2026-11-03 15:08:18 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.029 |  |
| 2026-11-03 15:05:18 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | -0.029 |  |
| 2026-11-03 16:02:22 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.040 |  |
| 2026-11-03 15:02:24 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | -0.044 |  |
| 2026-11-03 15:09:46 | Ellagawa (Kalu Ganga) | 6.45 | 🟢 Normal | -0.047 |  |
| 2026-11-03 15:03:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.76 | 🟢 Normal | -0.049 |  |
| 2026-11-03 15:07:55 | Rathnapura (Kalu Ganga) | 2.47 | 🟢 Normal | -0.065 |  |
| 2026-11-03 15:07:01 | Glencourse (Kelani Ganga) | 10.43 | 🟢 Normal | -0.082 |  |
| 2026-11-03 15:06:51 | Giriulla (Maha Oya) | 1.95 | 🟢 Normal | -0.095 |  |
| 2026-11-03 15:05:28 | Hanwella (Kelani Ganga) | 2.78 | 🟢 Normal | -0.097 |  |
| 2026-11-03 16:01:40 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | -0.112 |  |
| 2026-11-03 15:04:38 | Badalgama (Maha Oya) | 3.40 | 🟢 Normal | -0.117 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)