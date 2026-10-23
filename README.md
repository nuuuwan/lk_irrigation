# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--23_18:11:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **296,000 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 18:11:30 | Panadugama (Nilwala Ganga) | 4.20 | 🟢 Normal | -0.032 |  |
| 2026-10-23 18:10:20 | Baddegama (Gin Ganga) | 2.13 | 🟢 Normal | -0.027 |  |
| 2026-10-23 18:09:34 | Horowpothana (Yan Oya) | 2.52 | 🟢 Normal | -0.135 |  |
| 2026-10-23 18:09:01 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | -2.000 |  |
| 2026-10-23 18:08:47 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | -0.060 |  |
| 2026-10-23 18:08:43 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | -2.000 |  |
| 2026-10-23 18:07:04 | Magura (Kalu Ganga) | 1.81 | 🟢 Normal | -0.039 |  |
| 2026-10-23 18:05:59 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.019 |  |
| 2026-10-23 18:05:57 | Badalgama (Maha Oya) | 3.28 | 🟢 Normal | -0.030 |  |
| 2026-10-23 18:05:52 | Galgamuwa (Mee Oya) | 2.48 | 🟢 Normal | -0.048 |  |
| 2026-10-23 18:05:25 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-23 18:05:10 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-10-23 18:04:52 | Glencourse (Kelani Ganga) | 11.20 | 🟢 Normal | -0.082 |  |
| 2026-10-23 18:04:18 | Siyambalanduwa (Heda Oya) | 1.75 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-23 18:03:40 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | -0.030 |  |
| 2026-10-23 18:03:40 | Hanwella (Kelani Ganga) | 3.78 | 🟢 Normal | -0.039 |  |
| 2026-10-23 18:03:29 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -6.108 |  |
| 2026-10-23 18:03:26 | Dunamale (Aththanagalu Oya) | 2.35 | 🟢 Normal | -0.029 |  |
| 2026-10-23 18:03:20 | Moragaswewa (Deduru Oya) | 4.41 | 🟢 Normal | -0.081 |  |
| 2026-10-23 18:02:40 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | -0.060 |  |
| 2026-10-23 18:02:32 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.021 |  |
| 2026-10-23 18:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.73 | 🟢 Normal | -0.061 |  |
| 2026-10-23 18:02:13 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.080 |  |
| 2026-10-23 18:02:08 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-23 18:02:07 | Rathnapura (Kalu Ganga) | 3.06 | 🟢 Normal | -0.063 |  |
| 2026-10-23 18:01:59 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.006 |  |
| 2026-10-23 18:01:50 | Thanthirimale (Malwathu Oya) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-10-23 18:01:45 | Ellagawa (Kalu Ganga) | 7.27 | 🟢 Normal | -0.071 |  |
| 2026-10-23 18:01:40 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-10-23 18:01:28 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.011 |  |
| 2026-10-23 18:01:24 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-23 18:01:24 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-23 18:01:17 | Giriulla (Maha Oya) | 1.95 | 🟢 Normal | -0.058 |  |
| 2026-10-23 18:01:16 | Pitabeddara (Nilwala Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-10-23 18:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-10-23 18:00:49 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-10-23 18:00:39 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.067 |  |
| 2026-10-23 18:00:15 | Putupaula (Kalu Ganga) | 1.95 | 🟢 Normal | -0.043 |  |
| 2026-10-23 18:00:08 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 18:04:18 | Siyambalanduwa (Heda Oya) | 1.75 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-23 17:05:07 | Peradeniya (Mahaweli Ganga) | 2.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-23 18:01:24 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-23 18:01:16 | Pitabeddara (Nilwala Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-10-23 18:05:10 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-10-23 18:05:25 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-23 18:00:08 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-23 18:01:24 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-23 18:02:08 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-23 18:01:59 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.006 |  |
| 2026-10-23 18:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-10-23 18:01:40 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-10-23 18:01:50 | Thanthirimale (Malwathu Oya) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-10-23 18:01:28 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.011 |  |
| 2026-10-23 18:05:59 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.019 |  |
| 2026-10-23 18:02:32 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.021 |  |
| 2026-10-23 18:00:49 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-10-23 18:10:20 | Baddegama (Gin Ganga) | 2.13 | 🟢 Normal | -0.027 |  |
| 2026-10-23 18:03:26 | Dunamale (Aththanagalu Oya) | 2.35 | 🟢 Normal | -0.029 |  |
| 2026-10-23 18:03:40 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | -0.030 |  |
| 2026-10-23 18:05:57 | Badalgama (Maha Oya) | 3.28 | 🟢 Normal | -0.030 |  |
| 2026-10-23 18:11:30 | Panadugama (Nilwala Ganga) | 4.20 | 🟢 Normal | -0.032 |  |
| 2026-10-23 18:07:04 | Magura (Kalu Ganga) | 1.81 | 🟢 Normal | -0.039 |  |
| 2026-10-23 18:03:40 | Hanwella (Kelani Ganga) | 3.78 | 🟢 Normal | -0.039 |  |
| 2026-10-23 18:00:15 | Putupaula (Kalu Ganga) | 1.95 | 🟢 Normal | -0.043 |  |
| 2026-10-23 18:05:52 | Galgamuwa (Mee Oya) | 2.48 | 🟢 Normal | -0.048 |  |
| 2026-10-23 18:01:17 | Giriulla (Maha Oya) | 1.95 | 🟢 Normal | -0.058 |  |
| 2026-10-23 18:02:40 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | -0.060 |  |
| 2026-10-23 18:08:47 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | -0.060 |  |
| 2026-10-23 18:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.73 | 🟢 Normal | -0.061 |  |
| 2026-10-23 18:02:07 | Rathnapura (Kalu Ganga) | 3.06 | 🟢 Normal | -0.063 |  |
| 2026-10-23 18:00:39 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.067 |  |
| 2026-10-23 18:01:45 | Ellagawa (Kalu Ganga) | 7.27 | 🟢 Normal | -0.071 |  |
| 2026-10-23 18:02:13 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.080 |  |
| 2026-10-23 18:03:20 | Moragaswewa (Deduru Oya) | 4.41 | 🟢 Normal | -0.081 |  |
| 2026-10-23 18:04:52 | Glencourse (Kelani Ganga) | 11.20 | 🟢 Normal | -0.082 |  |
| 2026-10-23 18:09:34 | Horowpothana (Yan Oya) | 2.52 | 🟢 Normal | -0.135 |  |
| 2026-10-23 18:09:01 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | -2.000 |  |
| 2026-10-23 18:03:29 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -6.108 |  |

## River Water Level Charts by Station

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)