# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--17_02:02:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **317,866 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-17 02:02:37 | Manampitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.019 |  |
| 2026-11-17 02:02:35 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.003 |  |
| 2026-11-17 02:02:18 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-11-17 02:02:10 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-11-17 02:02:09 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | -0.010 |  |
| 2026-11-17 02:02:04 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-17 02:01:58 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-17 02:01:52 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-11-17 02:01:47 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-11-17 02:01:32 | Ellagawa (Kalu Ganga) | 5.23 | 🟢 Normal | -0.010 |  |
| 2026-11-17 02:01:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | -0.041 |  |
| 2026-11-17 02:01:16 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-17 02:01:14 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-17 02:01:10 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-17 01:36:42 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.026 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-17 01:03:02 | Glencourse (Kelani Ganga) | 10.27 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-17 01:11:03 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-11-17 02:01:16 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-17 02:02:04 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-17 02:02:10 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-11-17 00:01:51 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-17 01:03:01 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-11-17 02:01:52 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-11-16 18:04:42 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-11-17 00:20:41 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-11-17 00:13:14 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-17 01:03:08 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-17 02:01:47 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-11-17 01:05:34 | Moraketiya (Walawe Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-11-17 02:01:58 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-17 01:10:44 | Dunamale (Aththanagalu Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-17 02:01:10 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-17 01:06:58 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-17 00:16:34 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-16 18:00:40 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-17 01:00:36 | Peradeniya (Mahaweli Ganga) | 2.94 | 🟢 Normal | 0.000 |  |
| 2026-11-17 01:02:37 | Thalgahagoda (Nilwala Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-11-17 02:01:14 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-17 02:02:18 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-11-17 02:02:35 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.003 |  |
| 2026-11-17 01:06:30 | Rathnapura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-11-17 01:03:46 | Urawa (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-11-17 02:02:09 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | -0.010 |  |
| 2026-11-17 02:01:32 | Ellagawa (Kalu Ganga) | 5.23 | 🟢 Normal | -0.010 |  |
| 2026-11-17 00:00:40 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | -0.011 |  |
| 2026-11-17 02:02:37 | Manampitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.019 |  |
| 2026-11-17 01:03:34 | Hanwella (Kelani Ganga) | 2.02 | 🟢 Normal | -0.020 |  |
| 2026-11-17 01:19:53 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.026 |  |
| 2026-11-17 01:36:42 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.026 |  |
| 2026-11-17 01:14:06 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | -0.026 |  |
| 2026-11-17 01:02:48 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.030 |  |
| 2026-11-17 00:02:26 | Panadugama (Nilwala Ganga) | 4.17 | 🟢 Normal | -0.032 |  |
| 2026-11-16 18:02:17 | Weraganthota (Mahaweli Ganga) | -1.91 | 🟢 Normal | -0.041 |  |
| 2026-11-17 02:01:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | -0.041 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)