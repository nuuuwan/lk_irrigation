# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--31_07:04:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **302,758 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 07:04:22 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | -0.043 |  |
| 2026-10-31 07:04:19 | Glencourse (Kelani Ganga) | 10.64 | 🟢 Normal | -0.010 |  |
| 2026-10-31 07:04:07 | Hanwella (Kelani Ganga) | 2.73 | 🟢 Normal | -0.029 |  |
| 2026-10-31 07:03:33 | Dunamale (Aththanagalu Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-10-31 07:03:18 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-10-31 07:03:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.40 | 🟡 Alert | -0.209 |  |
| 2026-10-31 07:03:12 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-10-31 07:03:09 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 07:03:02 | Rathnapura (Kalu Ganga) | 2.35 | 🟢 Normal | -0.053 |  |
| 2026-10-31 07:02:59 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-10-31 07:02:56 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-31 07:02:50 | Giriulla (Maha Oya) | 1.80 | 🟢 Normal | -0.061 |  |
| 2026-10-31 07:02:49 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.011 |  |
| 2026-10-31 07:02:20 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-31 07:02:11 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.050 |  |
| 2026-10-31 07:02:06 | Panadugama (Nilwala Ganga) | 4.88 | 🟢 Normal | -0.042 |  |
| 2026-10-31 07:02:05 | Ellagawa (Kalu Ganga) | 7.06 | 🟢 Normal | -0.124 |  |
| 2026-10-31 07:01:33 | Pitabeddara (Nilwala Ganga) | 1.51 | 🟢 Normal | -0.021 |  |
| 2026-10-31 07:01:31 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | -0.030 |  |
| 2026-10-31 07:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-10-31 07:01:26 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | -0.005 |  |
| 2026-10-31 07:01:05 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-31 07:00:48 | Weraganthota (Mahaweli Ganga) | -2.96 | 🟢 Normal | -0.129 |  |
| 2026-10-31 07:00:29 | Magura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.100 |  |
| 2026-10-31 07:00:07 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-10-31 06:33:10 | Pitabeddara (Nilwala Ganga) | 1.52 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 06:04:54 | Thalgahagoda (Nilwala Ganga) | 1.70 | 🟠 Minor Flood | -0.028 |  |
| 2026-10-31 07:03:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.40 | 🟡 Alert | -0.209 |  |
| 2026-10-31 07:02:20 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-31 06:02:10 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-31 07:01:05 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-31 07:02:59 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-10-31 06:01:11 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-31 07:03:09 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:01:07 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-31 07:02:56 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-31 07:03:33 | Dunamale (Aththanagalu Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-10-31 06:04:29 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-31 06:08:16 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-31 07:01:26 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | -0.005 |  |
| 2026-10-31 07:04:19 | Glencourse (Kelani Ganga) | 10.64 | 🟢 Normal | -0.010 |  |
| 2026-10-31 06:06:57 | Baddegama (Gin Ganga) | 2.79 | 🟢 Normal | -0.010 |  |
| 2026-10-31 06:06:26 | Urawa (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-10-31 07:00:07 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-10-31 06:05:17 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-10-31 07:03:12 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-10-31 07:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-10-31 07:02:49 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.011 |  |
| 2026-10-31 06:01:30 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-10-31 06:01:02 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | -0.013 |  |
| 2026-10-31 07:03:18 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-10-31 07:01:33 | Pitabeddara (Nilwala Ganga) | 1.51 | 🟢 Normal | -0.021 |  |
| 2026-10-31 07:04:07 | Hanwella (Kelani Ganga) | 2.73 | 🟢 Normal | -0.029 |  |
| 2026-10-31 07:01:31 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | -0.030 |  |
| 2026-10-31 07:02:06 | Panadugama (Nilwala Ganga) | 4.88 | 🟢 Normal | -0.042 |  |
| 2026-10-31 07:04:22 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | -0.043 |  |
| 2026-10-31 07:02:11 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.050 |  |
| 2026-10-31 07:03:02 | Rathnapura (Kalu Ganga) | 2.35 | 🟢 Normal | -0.053 |  |
| 2026-10-31 06:05:48 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.060 |  |
| 2026-10-31 07:02:50 | Giriulla (Maha Oya) | 1.80 | 🟢 Normal | -0.061 |  |
| 2026-10-31 06:03:45 | Putupaula (Kalu Ganga) | 2.72 | 🟢 Normal | -0.062 |  |
| 2026-10-31 07:00:29 | Magura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.100 |  |
| 2026-10-31 06:05:46 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | -0.104 |  |
| 2026-10-31 07:02:05 | Ellagawa (Kalu Ganga) | 7.06 | 🟢 Normal | -0.124 |  |
| 2026-10-31 07:00:48 | Weraganthota (Mahaweli Ganga) | -2.96 | 🟢 Normal | -0.129 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)