# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--20_18:10:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **321,156 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-20 18:10:53 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-11-20 18:09:05 | Urawa (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.011 |  |
| 2026-11-20 18:08:41 | Panadugama (Nilwala Ganga) | 3.29 | 🟢 Normal | -0.011 |  |
| 2026-11-20 18:07:55 | Dunamale (Aththanagalu Oya) | 1.27 | 🟢 Normal | -0.009 |  |
| 2026-11-20 18:06:13 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-20 18:05:48 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-11-20 18:05:39 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | -0.019 |  |
| 2026-11-20 18:05:20 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-20 18:05:13 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-20 18:04:51 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.029 |  |
| 2026-11-20 18:03:53 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-11-20 18:03:49 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-11-20 18:03:33 | Glencourse (Kelani Ganga) | 9.33 | 🟢 Normal | -0.033 |  |
| 2026-11-20 18:03:22 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.116 |  |
| 2026-11-20 18:03:15 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.534 | 🔺 Rising |
| 2026-11-20 18:03:13 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | 0.000 |  |
| 2026-11-20 18:03:10 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-11-20 18:03:06 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-20 18:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | -0.031 |  |
| 2026-11-20 18:02:45 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-11-20 18:02:39 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-20 18:02:33 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.039 |  |
| 2026-11-20 18:02:25 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-20 18:02:18 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-11-20 18:02:12 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-20 18:01:56 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-20 18:01:45 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-20 18:01:40 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | -0.011 |  |
| 2026-11-20 18:01:39 | Rathnapura (Kalu Ganga) | 1.36 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-20 18:01:26 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-11-20 18:01:26 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.022 |  |
| 2026-11-20 18:01:14 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-11-20 18:00:58 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-20 18:00:42 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-11-20 18:00:28 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-11-20 18:00:22 | Horowpothana (Yan Oya) | 1.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-20 18:00:21 | Weraganthota (Mahaweli Ganga) | -2.17 | 🟢 Normal | -0.020 |  |
| 2026-11-20 18:00:18 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-20 18:03:15 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.534 | 🔺 Rising |
| 2026-11-20 18:05:48 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-11-20 18:01:39 | Rathnapura (Kalu Ganga) | 1.36 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-20 18:00:22 | Horowpothana (Yan Oya) | 1.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-20 18:00:58 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-20 18:05:13 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-20 18:00:18 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-20 18:03:06 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-20 18:02:39 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-20 18:02:12 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-20 18:00:42 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-11-20 18:02:25 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-20 18:03:13 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-20 18:05:20 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-20 18:01:45 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-20 18:03:53 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-11-20 18:06:13 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-20 18:02:45 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-11-20 18:01:56 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-20 18:07:55 | Dunamale (Aththanagalu Oya) | 1.27 | 🟢 Normal | -0.009 |  |
| 2026-11-20 18:02:18 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-11-20 18:01:14 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-11-20 18:03:10 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-11-20 18:00:28 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-11-20 18:01:26 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-11-20 18:08:41 | Panadugama (Nilwala Ganga) | 3.29 | 🟢 Normal | -0.011 |  |
| 2026-11-20 18:01:40 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | -0.011 |  |
| 2026-11-20 18:09:05 | Urawa (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.011 |  |
| 2026-11-20 18:05:39 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | -0.019 |  |
| 2026-11-20 18:10:53 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-11-20 18:00:21 | Weraganthota (Mahaweli Ganga) | -2.17 | 🟢 Normal | -0.020 |  |
| 2026-11-20 18:03:49 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-11-20 18:01:26 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.022 |  |
| 2026-11-20 18:04:51 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.029 |  |
| 2026-11-20 18:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | -0.031 |  |
| 2026-11-20 18:03:33 | Glencourse (Kelani Ganga) | 9.33 | 🟢 Normal | -0.033 |  |
| 2026-11-20 18:02:33 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.039 |  |
| 2026-11-20 18:03:22 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.116 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)