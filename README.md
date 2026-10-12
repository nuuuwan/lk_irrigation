# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--12_22:22:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **286,220 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Urawa — Alert; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 22:22:03 | Peradeniya (Mahaweli Ganga) | 3.02 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-12 22:19:56 | Norwood (Kelani Ganga) | 1.31 | 🟢 Normal | -0.090 |  |
| 2026-10-12 22:17:33 | Moragaswewa (Deduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-12 22:15:54 | Thawalama (Gin Ganga) | 3.27 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-12 22:10:10 | Baddegama (Gin Ganga) | 2.42 | 🟢 Normal | -0.028 |  |
| 2026-10-12 22:09:56 | Thalgahagoda (Nilwala Ganga) | 1.27 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-10-12 22:09:56 | Panadugama (Nilwala Ganga) | 5.61 | 🟡 Alert | 0.187 | 🔺 Rising |
| 2026-10-12 22:09:19 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-10-12 22:08:07 | Rathnapura (Kalu Ganga) | 3.37 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-10-12 22:07:28 | Moraketiya (Walawe Ganga) | 1.48 | 🟢 Normal | 0.402 | 🔺 Rising |
| 2026-10-12 22:07:11 | Urawa (Nilwala Ganga) | 3.05 | 🟡 Alert | 0.230 | 🔺 Rising |
| 2026-10-12 22:06:30 | Giriulla (Maha Oya) | 1.73 | 🟢 Normal | -0.029 |  |
| 2026-10-12 22:06:24 | Magura (Kalu Ganga) | 2.96 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-10-12 22:06:03 | Putupaula (Kalu Ganga) | 1.65 | 🟢 Normal | -0.070 |  |
| 2026-10-12 22:05:39 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.080 |  |
| 2026-10-12 22:05:07 | Glencourse (Kelani Ganga) | 11.71 | 🟢 Normal | -0.020 |  |
| 2026-10-12 22:04:59 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-12 22:04:14 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-10-12 22:04:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.14 | 🟡 Alert | 0.038 | 🔺 Rising |
| 2026-10-12 22:03:55 | Nagalagam Street (Kelani Ganga) | 0.41 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-12 22:03:52 | Dunamale (Aththanagalu Oya) | 2.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 22:03:49 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-10-12 22:03:39 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-12 22:03:20 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | -0.020 |  |
| 2026-10-12 22:03:08 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-10-12 22:03:05 | Pitabeddara (Nilwala Ganga) | 2.41 | 🟢 Normal | 0.457 | 🔺 Rising |
| 2026-10-12 22:02:38 | Ellagawa (Kalu Ganga) | 6.88 | 🟢 Normal | -0.021 |  |
| 2026-10-12 22:02:21 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 22:02:12 | Hanwella (Kelani Ganga) | 3.77 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-12 22:02:07 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-12 22:01:47 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-12 22:01:13 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 22:01:11 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-12 22:01:04 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-12 22:01:02 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 22:07:11 | Urawa (Nilwala Ganga) | 3.05 | 🟡 Alert | 0.230 | 🔺 Rising |
| 2026-10-12 22:09:56 | Panadugama (Nilwala Ganga) | 5.61 | 🟡 Alert | 0.187 | 🔺 Rising |
| 2026-10-12 22:04:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.14 | 🟡 Alert | 0.038 | 🔺 Rising |
| 2026-10-12 22:03:05 | Pitabeddara (Nilwala Ganga) | 2.41 | 🟢 Normal | 0.457 | 🔺 Rising |
| 2026-10-12 22:07:28 | Moraketiya (Walawe Ganga) | 1.48 | 🟢 Normal | 0.402 | 🔺 Rising |
| 2026-10-12 22:06:24 | Magura (Kalu Ganga) | 2.96 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-10-12 22:08:07 | Rathnapura (Kalu Ganga) | 3.37 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-10-12 22:04:14 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-10-12 22:03:55 | Nagalagam Street (Kelani Ganga) | 0.41 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-12 22:15:54 | Thawalama (Gin Ganga) | 3.27 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-12 22:02:12 | Hanwella (Kelani Ganga) | 3.77 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-12 22:22:03 | Peradeniya (Mahaweli Ganga) | 3.02 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-12 22:03:39 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-12 22:09:56 | Thalgahagoda (Nilwala Ganga) | 1.27 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-10-12 22:02:21 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 22:01:13 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 22:03:52 | Dunamale (Aththanagalu Oya) | 2.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 18:02:58 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | 0.000 |  |
| 2026-10-12 22:02:07 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-12 22:17:33 | Moragaswewa (Deduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-12 22:01:47 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-12 22:01:02 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:02:38 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-12 21:08:31 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-12 22:01:11 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-12 22:01:04 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:01:38 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-12 22:04:59 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-12 22:09:19 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-10-12 22:03:49 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-10-12 22:03:08 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-10-12 22:03:20 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | -0.020 |  |
| 2026-10-12 22:05:07 | Glencourse (Kelani Ganga) | 11.71 | 🟢 Normal | -0.020 |  |
| 2026-10-12 22:02:38 | Ellagawa (Kalu Ganga) | 6.88 | 🟢 Normal | -0.021 |  |
| 2026-10-12 22:10:10 | Baddegama (Gin Ganga) | 2.42 | 🟢 Normal | -0.028 |  |
| 2026-10-12 22:06:30 | Giriulla (Maha Oya) | 1.73 | 🟢 Normal | -0.029 |  |
| 2026-10-12 22:06:03 | Putupaula (Kalu Ganga) | 1.65 | 🟢 Normal | -0.070 |  |
| 2026-10-12 22:05:39 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.080 |  |
| 2026-10-12 22:19:56 | Norwood (Kelani Ganga) | 1.31 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)