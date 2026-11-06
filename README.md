# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--06_15:03:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **308,501 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 15:03:34 | Hanwella (Kelani Ganga) | 2.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 15:03:33 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | -0.019 |  |
| 2026-11-06 15:03:00 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-11-06 15:02:25 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.040 |  |
| 2026-11-06 15:02:16 | Moragaswewa (Deduru Oya) | 2.65 | 🟢 Normal | -0.065 |  |
| 2026-11-06 15:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-06 15:02:04 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 15:01:56 | Peradeniya (Mahaweli Ganga) | 2.69 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-06 15:01:28 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-11-06 15:01:19 | Giriulla (Maha Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-11-06 15:01:16 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-06 15:00:51 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-11-06 15:00:17 | Kuda Oya (Kirindi Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-11-06 15:00:13 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | -0.133 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 15:01:28 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-11-06 15:01:16 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-06 14:00:50 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-06 14:02:34 | Glencourse (Kelani Ganga) | 10.48 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-06 14:06:01 | Horowpothana (Yan Oya) | 2.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-06 15:01:56 | Peradeniya (Mahaweli Ganga) | 2.69 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-06 14:01:48 | Thanthirimale (Malwathu Oya) | 1.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 15:03:34 | Hanwella (Kelani Ganga) | 2.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 14:00:56 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-06 15:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-06 15:02:04 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 14:07:40 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-11-06 14:04:02 | Baddegama (Gin Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-11-06 15:03:00 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-11-06 14:02:48 | Putupaula (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-06 14:03:40 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-06 14:09:34 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-11-06 14:10:15 | Urawa (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-06 14:00:56 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-06 15:00:17 | Kuda Oya (Kirindi Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-11-06 14:02:56 | Thanamalwila (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-06 14:14:51 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | -0.008 |  |
| 2026-11-06 14:02:55 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-11-06 15:01:19 | Giriulla (Maha Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-11-06 14:02:13 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-11-06 15:00:51 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-11-06 14:07:03 | Rathnapura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.019 |  |
| 2026-11-06 15:03:33 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | -0.019 |  |
| 2026-11-06 14:08:18 | Panadugama (Nilwala Ganga) | 3.85 | 🟢 Normal | -0.019 |  |
| 2026-11-06 14:06:32 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | -0.020 |  |
| 2026-11-06 14:03:38 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.021 |  |
| 2026-11-06 14:01:46 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | -0.021 |  |
| 2026-11-06 14:09:17 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.027 |  |
| 2026-11-06 15:02:25 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.040 |  |
| 2026-11-06 14:03:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.05 | 🟢 Normal | -0.059 |  |
| 2026-11-06 15:02:16 | Moragaswewa (Deduru Oya) | 2.65 | 🟢 Normal | -0.065 |  |
| 2026-11-06 15:00:13 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | -0.133 |  |
| 2026-11-06 14:04:04 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.265 |  |
| 2026-11-06 14:04:20 | Magura (Kalu Ganga) | 1.92 | 🟢 Normal | -2.250 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)