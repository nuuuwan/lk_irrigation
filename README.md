# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--31_03:03:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **302,598 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 03:03:20 | Ellagawa (Kalu Ganga) | 7.50 | 🟢 Normal | -0.088 |  |
| 2026-10-31 03:03:02 | Glencourse (Kelani Ganga) | 10.71 | 🟢 Normal | -0.021 |  |
| 2026-10-31 03:02:33 | Thalgahagoda (Nilwala Ganga) | 1.75 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-31 03:02:26 | Pitabeddara (Nilwala Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-10-31 03:02:21 | Thanamalwila (Kirindi Oya) | 1.57 | 🟢 Normal | 0.292 | 🔺 Rising |
| 2026-10-31 03:02:09 | Hanwella (Kelani Ganga) | 2.81 | 🟢 Normal | -0.010 |  |
| 2026-10-31 03:01:41 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-31 03:01:38 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-10-31 03:01:38 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.060 |  |
| 2026-10-31 03:01:20 | Magura (Kalu Ganga) | 2.61 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-31 03:01:10 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-31 03:01:08 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.042 |  |
| 2026-10-31 02:28:31 | Panadugama (Nilwala Ganga) | 5.03 | 🟡 Alert | -0.007 |  |
| 2026-10-31 02:23:03 | Urawa (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.008 |  |
| 2026-10-31 02:19:53 | Magura (Kalu Ganga) | 2.57 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-31 02:19:52 | Magura (Kalu Ganga) | 2.52 | 🟢 Normal | 0.058 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 03:02:33 | Thalgahagoda (Nilwala Ganga) | 1.75 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-31 02:28:31 | Panadugama (Nilwala Ganga) | 5.03 | 🟡 Alert | -0.007 |  |
| 2026-10-31 00:01:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.06 | 🟡 Alert | -0.052 |  |
| 2026-10-31 03:02:21 | Thanamalwila (Kirindi Oya) | 1.57 | 🟢 Normal | 0.292 | 🔺 Rising |
| 2026-10-31 02:05:11 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-10-31 03:01:20 | Magura (Kalu Ganga) | 2.61 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-31 02:02:23 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-31 02:03:36 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-31 02:04:23 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-31 03:01:10 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-31 03:01:41 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-31 02:03:06 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-31 03:01:38 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:01:07 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-31 02:03:11 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-31 02:03:07 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-10-31 02:03:13 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-31 02:06:53 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-31 01:02:40 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-31 00:06:05 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.006 |  |
| 2026-10-31 02:23:03 | Urawa (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.008 |  |
| 2026-10-31 03:02:26 | Pitabeddara (Nilwala Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-10-31 03:02:09 | Hanwella (Kelani Ganga) | 2.81 | 🟢 Normal | -0.010 |  |
| 2026-10-30 18:00:09 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.021 |  |
| 2026-10-31 02:00:35 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.021 |  |
| 2026-10-30 18:00:42 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | -0.021 |  |
| 2026-10-31 03:03:02 | Glencourse (Kelani Ganga) | 10.71 | 🟢 Normal | -0.021 |  |
| 2026-10-31 02:01:54 | Thawalama (Gin Ganga) | 2.13 | 🟢 Normal | -0.024 |  |
| 2026-10-31 02:11:51 | Baddegama (Gin Ganga) | 2.90 | 🟢 Normal | -0.026 |  |
| 2026-10-31 02:03:37 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.028 |  |
| 2026-10-31 02:07:39 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | -0.033 |  |
| 2026-10-31 02:11:37 | Rathnapura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.034 |  |
| 2026-10-31 03:01:08 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.042 |  |
| 2026-10-31 00:04:18 | Padiyathalawa (Maduru Oya) | 1.38 | 🟢 Normal | -0.049 |  |
| 2026-10-31 02:03:51 | Putupaula (Kalu Ganga) | 2.95 | 🟢 Normal | -0.059 |  |
| 2026-10-31 03:01:38 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.060 |  |
| 2026-10-31 02:05:22 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.063 |  |
| 2026-10-31 03:03:20 | Ellagawa (Kalu Ganga) | 7.50 | 🟢 Normal | -0.088 |  |
| 2026-10-31 02:03:12 | Yaka Wewa (Ma Oya) | 0.00 | 🟢 Normal | -0.499 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)