# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--20_16:31:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **321,080 measurements** from **39** stations.
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
| 2026-11-20 16:31:31 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:17:37 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:15:54 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.008 |  |
| 2026-11-20 16:11:38 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:10:49 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.071 |  |
| 2026-11-20 16:10:18 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:09:02 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:08:43 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-20 16:08:39 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.029 |  |
| 2026-11-20 16:08:13 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:07:55 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:07:38 | Panadugama (Nilwala Ganga) | 3.30 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:05:52 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | -0.010 |  |
| 2026-11-20 16:05:40 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:04:36 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:04:21 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.059 |  |
| 2026-11-20 16:04:19 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:03:46 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-11-20 16:03:40 | Ellagawa (Kalu Ganga) | 4.71 | 🟢 Normal | -0.010 |  |
| 2026-11-20 16:03:38 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:03:30 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:03:23 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:03:14 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.23 | 🟢 Normal | -0.040 |  |
| 2026-11-20 16:02:37 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:02:34 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-11-20 16:02:25 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:02:20 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-20 16:02:20 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-11-20 16:02:17 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-11-20 16:01:54 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-11-20 16:01:45 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:01:43 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | -0.020 |  |
| 2026-11-20 16:01:37 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:01:30 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-20 16:01:20 | Weraganthota (Mahaweli Ganga) | -2.13 | 🟢 Normal | -0.079 |  |
| 2026-11-20 16:01:17 | Glencourse (Kelani Ganga) | 9.44 | 🟢 Normal | -0.062 |  |
| 2026-11-20 16:01:14 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:01:14 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:00:11 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-20 15:58:56 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-20 16:08:43 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-20 16:02:20 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-20 16:01:30 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-20 16:03:14 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:31:31 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:01:14 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:08:13 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:01:45 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:07:55 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:10:18 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:04:36 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:05:40 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:01:37 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:03:30 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:07:38 | Panadugama (Nilwala Ganga) | 3.30 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:09:02 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:17:37 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:03:38 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:02:25 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:03:23 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:11:38 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:01:14 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:00:11 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-20 16:15:54 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.008 |  |
| 2026-11-20 16:05:52 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | -0.010 |  |
| 2026-11-20 16:01:54 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-11-20 16:03:40 | Ellagawa (Kalu Ganga) | 4.71 | 🟢 Normal | -0.010 |  |
| 2026-11-20 16:02:20 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-11-20 16:02:34 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-11-20 16:03:46 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-11-20 16:01:43 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | -0.020 |  |
| 2026-11-20 16:02:17 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-11-20 16:08:39 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.029 |  |
| 2026-11-20 16:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.23 | 🟢 Normal | -0.040 |  |
| 2026-11-20 16:04:21 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.059 |  |
| 2026-11-20 16:01:17 | Glencourse (Kelani Ganga) | 9.44 | 🟢 Normal | -0.062 |  |
| 2026-11-20 16:10:49 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.071 |  |
| 2026-11-20 16:01:20 | Weraganthota (Mahaweli Ganga) | -2.13 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)