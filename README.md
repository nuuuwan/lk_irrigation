# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--15_10:03:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **316,392 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-15 10:03:30 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | -0.070 |  |
| 2026-11-15 10:03:28 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-11-15 10:03:06 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-15 10:02:54 | Kuda Oya (Kirindi Oya) | 1.80 | 🟢 Normal | -0.020 |  |
| 2026-11-15 10:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.30 | 🟢 Normal | 0.000 |  |
| 2026-11-15 10:02:37 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | -0.011 |  |
| 2026-11-15 10:02:34 | Hanwella (Kelani Ganga) | 2.50 | 🟢 Normal | -0.010 |  |
| 2026-11-15 10:02:25 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-15 10:02:18 | Moraketiya (Walawe Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-11-15 10:02:16 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-11-15 10:02:13 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.101 |  |
| 2026-11-15 10:02:12 | Thanamalwila (Kirindi Oya) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-11-15 10:01:56 | Manampitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-11-15 10:01:54 | Rathnapura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.032 |  |
| 2026-11-15 10:01:45 | Baddegama (Gin Ganga) | 2.71 | 🟢 Normal | -0.042 |  |
| 2026-11-15 10:01:08 | Peradeniya (Mahaweli Ganga) | 2.92 | 🟢 Normal | -0.050 |  |
| 2026-11-15 10:00:58 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.093 |  |
| 2026-11-15 10:00:52 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.053 |  |
| 2026-11-15 10:00:37 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-11-15 10:00:36 | Ellagawa (Kalu Ganga) | 5.66 | 🟢 Normal | 0.000 |  |
| 2026-11-15 10:00:35 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-15 09:28:03 | Thalgahagoda (Nilwala Ganga) | 1.84 | 🟠 Minor Flood | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-15 09:28:03 | Thalgahagoda (Nilwala Ganga) | 1.84 | 🟠 Minor Flood | -0.021 |  |
| 2026-11-15 09:01:27 | Weraganthota (Mahaweli Ganga) | -2.15 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-15 09:03:33 | Moragaswewa (Deduru Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-15 09:01:48 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-15 10:03:06 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-15 10:02:16 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-11-15 09:05:45 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-11-15 09:01:48 | Pitabeddara (Nilwala Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-15 10:00:36 | Ellagawa (Kalu Ganga) | 5.66 | 🟢 Normal | 0.000 |  |
| 2026-11-15 09:08:33 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-15 10:02:18 | Moraketiya (Walawe Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-11-15 10:00:35 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-15 09:03:32 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-11-15 09:04:00 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-11-15 10:02:25 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-15 09:01:44 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-15 10:01:56 | Manampitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-11-15 10:00:37 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-11-15 10:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.30 | 🟢 Normal | 0.000 |  |
| 2026-11-15 09:05:00 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-11-15 10:02:12 | Thanamalwila (Kirindi Oya) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-11-15 10:03:28 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-11-15 10:02:34 | Hanwella (Kelani Ganga) | 2.50 | 🟢 Normal | -0.010 |  |
| 2026-11-15 09:06:36 | Badalgama (Maha Oya) | 2.84 | 🟢 Normal | -0.010 |  |
| 2026-11-15 09:08:38 | Magura (Kalu Ganga) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-11-15 10:02:37 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | -0.011 |  |
| 2026-11-15 09:03:30 | Urawa (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.011 |  |
| 2026-11-15 10:02:54 | Kuda Oya (Kirindi Oya) | 1.80 | 🟢 Normal | -0.020 |  |
| 2026-11-15 09:05:00 | Panadugama (Nilwala Ganga) | 4.83 | 🟢 Normal | -0.022 |  |
| 2026-11-15 09:07:19 | Glencourse (Kelani Ganga) | 10.63 | 🟢 Normal | -0.030 |  |
| 2026-11-15 09:01:30 | Wellawaya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.030 |  |
| 2026-11-15 10:01:54 | Rathnapura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.032 |  |
| 2026-11-15 10:01:45 | Baddegama (Gin Ganga) | 2.71 | 🟢 Normal | -0.042 |  |
| 2026-11-15 10:01:08 | Peradeniya (Mahaweli Ganga) | 2.92 | 🟢 Normal | -0.050 |  |
| 2026-11-15 10:00:52 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.053 |  |
| 2026-11-15 10:03:30 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | -0.070 |  |
| 2026-11-15 09:10:36 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | -0.071 |  |
| 2026-11-15 10:00:58 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.093 |  |
| 2026-11-15 10:02:13 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)