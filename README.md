# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--14_05:03:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **287,326 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟡 Magura — Alert; 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 05:03:17 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.058 |  |
| 2026-10-14 05:02:52 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-10-14 05:02:38 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-14 05:02:36 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-14 05:02:31 | Thawalama (Gin Ganga) | 3.34 | 🟢 Normal | -0.078 |  |
| 2026-10-14 05:02:18 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-10-14 05:01:44 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-14 05:01:38 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-14 05:01:17 | Ellagawa (Kalu Ganga) | 7.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-14 05:01:05 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-10-14 05:01:01 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-14 05:00:53 | Pitabeddara (Nilwala Ganga) | 2.90 | 🟢 Normal | -0.410 |  |
| 2026-10-14 05:00:52 | Moragaswewa (Deduru Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-14 04:31:39 | Pitabeddara (Nilwala Ganga) | 3.10 | 🟢 Normal | -0.410 |  |
| 2026-10-14 04:31:06 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-10-14 04:29:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.90 | 🟢 Normal | -0.014 |  |
| 2026-10-14 04:22:12 | Moraketiya (Walawe Ganga) | 1.61 | 🟢 Normal | -0.067 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 04:12:49 | Panadugama (Nilwala Ganga) | 6.09 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-14 04:03:03 | Magura (Kalu Ganga) | 5.36 | 🟡 Alert | 0.159 | 🔺 Rising |
| 2026-10-14 04:03:20 | Thalgahagoda (Nilwala Ganga) | 1.68 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-10-14 04:06:02 | Putupaula (Kalu Ganga) | 1.85 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-10-14 04:09:32 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-10-14 04:04:51 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-14 04:02:29 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-14 05:01:17 | Ellagawa (Kalu Ganga) | 7.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-14 04:03:55 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-14 05:02:36 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-14 04:02:14 | Hanwella (Kelani Ganga) | 3.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 03:07:14 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-14 04:05:41 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-14 05:01:01 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-14 05:00:52 | Moragaswewa (Deduru Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-14 05:01:38 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-14 05:02:52 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:05:16 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-14 03:06:06 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-14 04:05:13 | Dunamale (Aththanagalu Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-10-14 05:02:38 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-14 05:01:44 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-14 03:56:22 | Rathnapura (Kalu Ganga) | 4.32 | 🟢 Normal | -0.005 |  |
| 2026-10-13 18:04:16 | Thanthirimale (Malwathu Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-10-14 01:06:58 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-10-13 18:00:31 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.010 |  |
| 2026-10-14 04:29:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.90 | 🟢 Normal | -0.014 |  |
| 2026-10-14 04:04:24 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.016 |  |
| 2026-10-14 05:02:18 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-10-14 05:01:05 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-10-14 04:14:52 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | -0.029 |  |
| 2026-10-14 04:14:35 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | -0.033 |  |
| 2026-10-14 05:03:17 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.058 |  |
| 2026-10-14 04:10:37 | Glencourse (Kelani Ganga) | 11.06 | 🟢 Normal | -0.062 |  |
| 2026-10-14 04:22:12 | Moraketiya (Walawe Ganga) | 1.61 | 🟢 Normal | -0.067 |  |
| 2026-10-14 05:02:31 | Thawalama (Gin Ganga) | 3.34 | 🟢 Normal | -0.078 |  |
| 2026-10-14 04:09:53 | Urawa (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.082 |  |
| 2026-10-14 05:00:53 | Pitabeddara (Nilwala Ganga) | 2.90 | 🟢 Normal | -0.410 |  |
| 2026-10-14 04:04:58 | Baddegama (Gin Ganga) | 2.63 | 🟢 Normal | -1.218 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)