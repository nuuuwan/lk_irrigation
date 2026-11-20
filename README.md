# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--20_15:34:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **321,039 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-20 15:34:04 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:12:43 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:12:03 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:08:05 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:07:53 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | -0.009 |  |
| 2026-11-20 15:07:00 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:06:32 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:06:08 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:05:14 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:04:58 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:04:56 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:04:46 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.029 |  |
| 2026-11-20 15:04:35 | Panadugama (Nilwala Ganga) | 3.30 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:04:13 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:04:10 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:03:46 | Ellagawa (Kalu Ganga) | 4.72 | 🟢 Normal | -0.010 |  |
| 2026-11-20 15:03:43 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-20 15:03:39 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:03:28 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:03:23 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-11-20 15:03:11 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:03:09 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:03:01 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | -0.049 |  |
| 2026-11-20 15:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.27 | 🟢 Normal | -0.040 |  |
| 2026-11-20 15:02:49 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.052 |  |
| 2026-11-20 15:02:44 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:02:43 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-11-20 15:02:41 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-11-20 15:02:34 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-11-20 15:02:28 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:02:15 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | -0.030 |  |
| 2026-11-20 15:02:11 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-11-20 15:02:08 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:01:58 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-20 15:01:54 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-11-20 15:01:29 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:01:18 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:01:02 | Manampitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:00:46 | Moraketiya (Walawe Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:00:27 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:00:17 | Weraganthota (Mahaweli Ganga) | -2.05 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-20 15:01:58 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-20 15:03:43 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-20 15:06:32 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:03:11 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:00:27 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:01:29 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:02:44 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:02:08 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:04:10 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:07:00 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:06:08 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:12:43 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:03:28 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:08:05 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:04:35 | Panadugama (Nilwala Ganga) | 3.30 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:00:46 | Moraketiya (Walawe Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:02:28 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:05:14 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:01:18 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:04:13 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:01:02 | Manampitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:03:09 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:04:58 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:34:04 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:07:53 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | -0.009 |  |
| 2026-11-20 15:03:23 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-11-20 15:02:43 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-11-20 15:03:46 | Ellagawa (Kalu Ganga) | 4.72 | 🟢 Normal | -0.010 |  |
| 2026-11-20 15:02:11 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-11-20 15:01:54 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-11-20 15:02:41 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-11-20 15:02:34 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-11-20 15:00:17 | Weraganthota (Mahaweli Ganga) | -2.05 | 🟢 Normal | -0.020 |  |
| 2026-11-20 15:04:46 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.029 |  |
| 2026-11-20 15:02:15 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | -0.030 |  |
| 2026-11-20 15:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.27 | 🟢 Normal | -0.040 |  |
| 2026-11-20 15:03:01 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | -0.049 |  |
| 2026-11-20 15:02:49 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.052 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)