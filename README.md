# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--16_00:12:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **316,940 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-16 00:12:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.20 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:11:45 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:11:34 | Panadugama (Nilwala Ganga) | 4.64 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:11:33 | Urawa (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:11:11 | Urawa (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:11:05 | Rathnapura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.025 |  |
| 2026-11-16 00:09:38 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-11-16 00:08:55 | Moraketiya (Walawe Ganga) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:07:01 | Panadugama (Nilwala Ganga) | 4.64 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:06:14 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:06:05 | Thanamalwila (Kirindi Oya) | 1.50 | 🟢 Normal | -0.018 |  |
| 2026-11-16 00:05:40 | Baddegama (Gin Ganga) | 2.37 | 🟢 Normal | -0.010 |  |
| 2026-11-16 00:05:25 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-16 00:05:21 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | -0.010 |  |
| 2026-11-16 00:05:19 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:05:19 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-16 00:05:13 | Dunamale (Aththanagalu Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:05:01 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:05:00 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:04:21 | Hanwella (Kelani Ganga) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:04:01 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:03:48 | Ellagawa (Kalu Ganga) | 5.45 | 🟢 Normal | -0.010 |  |
| 2026-11-16 00:03:42 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:03:34 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-11-16 00:03:33 | Thalgahagoda (Nilwala Ganga) | 1.66 | 🟡 Alert | -0.021 |  |
| 2026-11-16 00:03:32 | Magura (Kalu Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:03:17 | Giriulla (Maha Oya) | 1.45 | 🟢 Normal | -0.011 |  |
| 2026-11-16 00:03:16 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | -0.030 |  |
| 2026-11-16 00:03:10 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:02:07 | Badalgama (Maha Oya) | 2.76 | 🟢 Normal | -0.011 |  |
| 2026-11-16 00:02:01 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.020 |  |
| 2026-11-16 00:01:28 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | -0.040 |  |
| 2026-11-16 00:01:24 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:01:24 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:01:22 | Moragaswewa (Deduru Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-11-16 00:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-11-16 00:01:01 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:00:39 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.005 |  |
| 2026-11-15 23:51:55 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-16 00:03:33 | Thalgahagoda (Nilwala Ganga) | 1.66 | 🟡 Alert | -0.021 |  |
| 2026-11-16 00:09:38 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-11-16 00:05:25 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-16 00:05:19 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-16 00:04:01 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:03:10 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-15 22:01:59 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:03:32 | Magura (Kalu Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:11:45 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:04:21 | Hanwella (Kelani Ganga) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:11:34 | Panadugama (Nilwala Ganga) | 4.64 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:05:19 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:08:55 | Moraketiya (Walawe Ganga) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:01:24 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:05:13 | Dunamale (Aththanagalu Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:01:01 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:06:14 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:05:00 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-15 18:00:37 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:11:33 | Urawa (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:01:24 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:12:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.20 | 🟢 Normal | 0.000 |  |
| 2026-11-16 00:00:39 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.005 |  |
| 2026-11-16 00:05:21 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | -0.010 |  |
| 2026-11-16 00:03:48 | Ellagawa (Kalu Ganga) | 5.45 | 🟢 Normal | -0.010 |  |
| 2026-11-16 00:05:40 | Baddegama (Gin Ganga) | 2.37 | 🟢 Normal | -0.010 |  |
| 2026-11-16 00:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-11-16 00:01:22 | Moragaswewa (Deduru Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-11-16 00:02:07 | Badalgama (Maha Oya) | 2.76 | 🟢 Normal | -0.011 |  |
| 2026-11-16 00:03:17 | Giriulla (Maha Oya) | 1.45 | 🟢 Normal | -0.011 |  |
| 2026-11-15 18:01:22 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-11-16 00:03:34 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-11-15 23:51:55 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.013 |  |
| 2026-11-16 00:06:05 | Thanamalwila (Kirindi Oya) | 1.50 | 🟢 Normal | -0.018 |  |
| 2026-11-16 00:02:01 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.020 |  |
| 2026-11-16 00:11:05 | Rathnapura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.025 |  |
| 2026-11-16 00:03:16 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | -0.030 |  |
| 2026-11-16 00:01:28 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | -0.040 |  |
| 2026-11-15 18:01:59 | Weraganthota (Mahaweli Ganga) | -1.94 | 🟢 Normal | -0.181 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)