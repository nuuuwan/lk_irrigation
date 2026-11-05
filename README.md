# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--06_02:29:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **308,015 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 02:29:00 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-11-06 02:25:24 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.486 |  |
| 2026-11-06 02:24:10 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.486 |  |
| 2026-11-06 02:22:05 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 02:12:53 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 02:11:10 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.019 |  |
| 2026-11-06 02:07:17 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-06 02:06:48 | Badalgama (Maha Oya) | 3.27 | 🟢 Normal | 0.000 |  |
| 2026-11-06 02:06:20 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-06 02:05:47 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.035 |  |
| 2026-11-06 02:05:29 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.005 |  |
| 2026-11-06 02:05:06 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.039 |  |
| 2026-11-06 02:04:37 | Manampitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-11-06 02:04:32 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | -0.409 |  |
| 2026-11-06 02:04:28 | Rathnapura (Kalu Ganga) | 2.84 | 🟢 Normal | -0.035 |  |
| 2026-11-06 02:03:43 | Hanwella (Kelani Ganga) | 2.45 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-06 02:03:38 | Giriulla (Maha Oya) | 1.94 | 🟢 Normal | -0.041 |  |
| 2026-11-06 02:03:28 | Thalgahagoda (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-06 02:03:23 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-11-06 02:03:12 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-11-06 02:03:11 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-11-06 02:02:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.64 | 🟢 Normal | -0.079 |  |
| 2026-11-06 02:02:55 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-11-06 02:02:28 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-11-06 02:02:00 | Peradeniya (Mahaweli Ganga) | 2.77 | 🟢 Normal | -0.010 |  |
| 2026-11-06 02:01:54 | Moragaswewa (Deduru Oya) | 3.00 | 🟢 Normal | -0.100 |  |
| 2026-11-06 02:01:51 | Panadugama (Nilwala Ganga) | 4.24 | 🟢 Normal | 0.000 |  |
| 2026-11-06 02:01:50 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-11-06 02:01:23 | Panadugama (Nilwala Ganga) | 4.24 | 🟢 Normal | 0.000 |  |
| 2026-11-06 02:00:27 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-06 02:00:22 | Glencourse (Kelani Ganga) | 10.50 | 🟢 Normal | -0.010 |  |
| 2026-11-06 02:00:19 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 01:59:50 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 02:06:20 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-06 02:03:43 | Hanwella (Kelani Ganga) | 2.45 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-06 01:04:44 | Putupaula (Kalu Ganga) | 1.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-06 02:00:19 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 02:00:27 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-06 00:09:57 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-06 02:22:05 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 02:07:17 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:03:39 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-06 02:03:11 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-11-06 01:04:18 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-06 02:01:51 | Panadugama (Nilwala Ganga) | 4.24 | 🟢 Normal | 0.000 |  |
| 2026-11-06 02:02:28 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-11-06 01:03:27 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-11-06 02:06:48 | Badalgama (Maha Oya) | 3.27 | 🟢 Normal | 0.000 |  |
| 2026-11-06 02:04:37 | Manampitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-11-06 02:29:00 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-11-06 01:03:58 | Urawa (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-06 02:03:28 | Thalgahagoda (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-06 02:05:29 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.005 |  |
| 2026-11-06 00:32:20 | Thanamalwila (Kirindi Oya) | 1.90 | 🟢 Normal | -0.007 |  |
| 2026-11-06 02:03:12 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-11-06 02:02:55 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-11-06 02:01:50 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-11-06 02:00:22 | Glencourse (Kelani Ganga) | 10.50 | 🟢 Normal | -0.010 |  |
| 2026-11-06 02:02:00 | Peradeniya (Mahaweli Ganga) | 2.77 | 🟢 Normal | -0.010 |  |
| 2026-11-05 18:01:46 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | -0.012 |  |
| 2026-11-06 02:11:10 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.019 |  |
| 2026-11-06 02:04:28 | Rathnapura (Kalu Ganga) | 2.84 | 🟢 Normal | -0.035 |  |
| 2026-11-06 02:05:47 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.035 |  |
| 2026-11-06 02:05:06 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.039 |  |
| 2026-11-06 02:03:38 | Giriulla (Maha Oya) | 1.94 | 🟢 Normal | -0.041 |  |
| 2026-11-05 18:01:57 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.049 |  |
| 2026-11-06 02:02:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.64 | 🟢 Normal | -0.079 |  |
| 2026-11-06 00:04:54 | Magura (Kalu Ganga) | 2.69 | 🟢 Normal | -0.092 |  |
| 2026-11-06 02:01:54 | Moragaswewa (Deduru Oya) | 3.00 | 🟢 Normal | -0.100 |  |
| 2026-11-06 02:04:32 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | -0.409 |  |
| 2026-11-06 02:25:24 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.486 |  |
| 2026-11-06 01:03:05 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | -28.315 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)