# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--23_22:23:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **296,143 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 22:23:34 | Pitabeddara (Nilwala Ganga) | 1.39 | 🟢 Normal | -0.008 |  |
| 2026-10-23 22:12:09 | Baddegama (Gin Ganga) | 2.00 | 🟢 Normal | -0.029 |  |
| 2026-10-23 22:10:19 | Panadugama (Nilwala Ganga) | 4.10 | 🟢 Normal | -0.038 |  |
| 2026-10-23 22:08:07 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-23 22:07:46 | Urawa (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-23 22:05:54 | Siyambalanduwa (Heda Oya) | 1.07 | 🟢 Normal | -0.029 |  |
| 2026-10-23 22:05:49 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | -0.011 |  |
| 2026-10-23 22:05:08 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | -0.019 |  |
| 2026-10-23 22:05:06 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-23 22:04:37 | Peradeniya (Mahaweli Ganga) | 2.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-23 22:04:37 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-10-23 22:03:58 | Badalgama (Maha Oya) | 3.17 | 🟢 Normal | -0.019 |  |
| 2026-10-23 22:03:51 | Rathnapura (Kalu Ganga) | 2.80 | 🟢 Normal | -0.062 |  |
| 2026-10-23 22:03:50 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-23 22:03:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.62 | 🟢 Normal | -0.034 |  |
| 2026-10-23 22:03:22 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-10-23 22:03:21 | Putupaula (Kalu Ganga) | 1.90 | 🟢 Normal | -0.011 |  |
| 2026-10-23 22:03:12 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-23 22:03:02 | Dunamale (Aththanagalu Oya) | 2.24 | 🟢 Normal | -0.020 |  |
| 2026-10-23 22:03:01 | Glencourse (Kelani Ganga) | 11.14 | 🟢 Normal | 0.000 |  |
| 2026-10-23 22:02:33 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-10-23 22:02:27 | Hanwella (Kelani Ganga) | 3.60 | 🟢 Normal | -0.030 |  |
| 2026-10-23 22:02:27 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-23 22:02:13 | Deraniyagala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-23 22:01:59 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-10-23 22:01:38 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-23 22:01:34 | Manampitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.065 |  |
| 2026-10-23 22:01:22 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | -1.954 |  |
| 2026-10-23 22:01:21 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-10-23 22:01:19 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-23 22:00:55 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | -0.035 |  |
| 2026-10-23 22:00:10 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 22:02:13 | Deraniyagala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-23 22:01:19 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-23 22:04:37 | Peradeniya (Mahaweli Ganga) | 2.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-23 22:03:12 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-23 22:08:07 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-23 22:01:38 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-23 22:02:27 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-23 22:00:10 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-23 22:03:01 | Glencourse (Kelani Ganga) | 11.14 | 🟢 Normal | 0.000 |  |
| 2026-10-23 22:03:50 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-23 22:05:06 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-23 22:04:37 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-10-23 22:07:46 | Urawa (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-23 22:02:33 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-10-23 22:23:34 | Pitabeddara (Nilwala Ganga) | 1.39 | 🟢 Normal | -0.008 |  |
| 2026-10-23 22:03:22 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-10-23 22:01:21 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-10-23 18:01:50 | Thanthirimale (Malwathu Oya) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-10-23 22:05:49 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | -0.011 |  |
| 2026-10-23 22:03:21 | Putupaula (Kalu Ganga) | 1.90 | 🟢 Normal | -0.011 |  |
| 2026-10-23 22:05:08 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | -0.019 |  |
| 2026-10-23 22:03:58 | Badalgama (Maha Oya) | 3.17 | 🟢 Normal | -0.019 |  |
| 2026-10-23 22:03:02 | Dunamale (Aththanagalu Oya) | 2.24 | 🟢 Normal | -0.020 |  |
| 2026-10-23 22:01:59 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-10-23 22:05:54 | Siyambalanduwa (Heda Oya) | 1.07 | 🟢 Normal | -0.029 |  |
| 2026-10-23 22:12:09 | Baddegama (Gin Ganga) | 2.00 | 🟢 Normal | -0.029 |  |
| 2026-10-23 21:02:44 | Ellagawa (Kalu Ganga) | 7.16 | 🟢 Normal | -0.030 |  |
| 2026-10-23 22:02:27 | Hanwella (Kelani Ganga) | 3.60 | 🟢 Normal | -0.030 |  |
| 2026-10-23 22:03:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.62 | 🟢 Normal | -0.034 |  |
| 2026-10-23 22:00:55 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | -0.035 |  |
| 2026-10-23 21:06:03 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.037 |  |
| 2026-10-23 22:10:19 | Panadugama (Nilwala Ganga) | 4.10 | 🟢 Normal | -0.038 |  |
| 2026-10-23 18:05:52 | Galgamuwa (Mee Oya) | 2.48 | 🟢 Normal | -0.048 |  |
| 2026-10-23 22:03:51 | Rathnapura (Kalu Ganga) | 2.80 | 🟢 Normal | -0.062 |  |
| 2026-10-23 22:01:34 | Manampitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.065 |  |
| 2026-10-23 21:00:12 | Moragaswewa (Deduru Oya) | 4.20 | 🟢 Normal | -0.081 |  |
| 2026-10-23 20:01:32 | Padiyathalawa (Maduru Oya) | 1.22 | 🟢 Normal | -0.234 |  |
| 2026-10-23 22:01:22 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | -1.954 |  |
| 2026-10-23 18:03:29 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -6.108 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)