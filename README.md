# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--05_21:03:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **307,818 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **12** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 21:03:19 | Giriulla (Maha Oya) | 2.10 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-05 21:03:09 | Moraketiya (Walawe Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-11-05 21:02:47 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | -39.130 |  |
| 2026-11-05 21:02:45 | Panadugama (Nilwala Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-11-05 21:02:27 | Moragaswewa (Deduru Oya) | 3.26 | 🟢 Normal | 0.000 |  |
| 2026-11-05 21:02:19 | Manampitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.029 |  |
| 2026-11-05 21:02:16 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-05 21:02:16 | Wellawaya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-11-05 21:01:27 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-05 21:01:26 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-11-05 21:01:15 | Peradeniya (Mahaweli Ganga) | 3.72 | 🟢 Normal | -39.130 |  |
| 2026-11-05 21:00:56 | Moragaswewa (Deduru Oya) | 3.26 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 20:05:52 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-11-05 19:20:36 | Magura (Kalu Ganga) | 2.56 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-11-05 20:03:09 | Glencourse (Kelani Ganga) | 10.40 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-05 21:03:19 | Giriulla (Maha Oya) | 2.10 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-05 20:01:35 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 21:02:16 | Wellawaya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-11-05 21:02:27 | Moragaswewa (Deduru Oya) | 3.26 | 🟢 Normal | 0.000 |  |
| 2026-11-05 21:02:16 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-05 20:02:30 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-05 20:01:36 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:03:39 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-05 20:15:28 | Pitabeddara (Nilwala Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-11-05 21:02:45 | Panadugama (Nilwala Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-11-05 20:03:22 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-05 21:03:09 | Moraketiya (Walawe Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-11-05 20:03:14 | Dunamale (Aththanagalu Oya) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-11-05 20:03:04 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-05 20:09:10 | Urawa (Nilwala Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-05 21:01:27 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-05 20:03:10 | Kuda Oya (Kirindi Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-11-05 20:03:18 | Thanamalwila (Kirindi Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-11-05 20:05:34 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-11-05 21:01:26 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-11-05 20:02:35 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-11-05 18:01:46 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | -0.012 |  |
| 2026-11-05 20:13:54 | Putupaula (Kalu Ganga) | 1.33 | 🟢 Normal | -0.017 |  |
| 2026-11-05 20:11:37 | Rathnapura (Kalu Ganga) | 2.70 | 🟢 Normal | -0.019 |  |
| 2026-11-05 20:06:01 | Badalgama (Maha Oya) | 3.22 | 🟢 Normal | -0.020 |  |
| 2026-11-05 20:10:56 | Ellagawa (Kalu Ganga) | 6.57 | 🟢 Normal | -0.026 |  |
| 2026-11-05 21:02:19 | Manampitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.029 |  |
| 2026-11-05 20:10:45 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | -0.030 |  |
| 2026-11-05 20:00:11 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.031 |  |
| 2026-11-05 20:02:31 | Hanwella (Kelani Ganga) | 2.30 | 🟢 Normal | -0.034 |  |
| 2026-11-05 20:06:18 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | -0.039 |  |
| 2026-11-05 20:02:24 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.041 |  |
| 2026-11-05 18:01:57 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.049 |  |
| 2026-11-05 20:09:16 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.060 |  |
| 2026-11-05 20:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.84 | 🟢 Normal | -0.065 |  |
| 2026-11-05 21:02:47 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | -39.130 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)