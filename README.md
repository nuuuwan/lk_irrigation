# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--11_22:02:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **313,241 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Urawa — Alert; 🟡 Thawalama — Alert; 🟡 Magura — Alert; 🟡 Moraketiya — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **10** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 22:02:54 | Putupaula (Kalu Ganga) | 2.63 | 🟢 Normal | -0.010 |  |
| 2026-11-11 22:02:32 | Panadugama (Nilwala Ganga) | 5.40 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-11-11 22:02:11 | Thanamalwila (Kirindi Oya) | 2.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-11 22:01:31 | Kuda Oya (Kirindi Oya) | 2.11 | 🟢 Normal | -0.051 |  |
| 2026-11-11 22:01:29 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | -0.025 |  |
| 2026-11-11 22:01:28 | Peradeniya (Mahaweli Ganga) | 4.75 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-11 22:01:27 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.063 |  |
| 2026-11-11 22:01:26 | Wellawaya (Kirindi Oya) | 2.64 | 🟢 Normal | 0.487 | 🔺 Rising |
| 2026-11-11 22:01:26 | Moragaswewa (Deduru Oya) | 3.65 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-11 22:00:05 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.050 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 21:04:09 | Baddegama (Gin Ganga) | 4.08 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 21:05:18 | Thalgahagoda (Nilwala Ganga) | 1.78 | 🟠 Minor Flood | -0.013 |  |
| 2026-11-11 21:03:25 | Urawa (Nilwala Ganga) | 2.75 | 🟡 Alert | 0.957 | 🔺 Rising |
| 2026-11-11 21:02:17 | Thawalama (Gin Ganga) | 4.86 | 🟡 Alert | 0.261 | 🔺 Rising |
| 2026-11-11 21:02:34 | Magura (Kalu Ganga) | 4.96 | 🟡 Alert | 0.151 | 🔺 Rising |
| 2026-11-11 21:01:06 | Moraketiya (Walawe Ganga) | 4.20 | 🟡 Alert | 0.107 | 🔺 Rising |
| 2026-11-11 21:03:31 | Dunamale (Aththanagalu Oya) | 3.86 | 🟡 Alert | 0.079 | 🔺 Rising |
| 2026-11-11 22:02:32 | Panadugama (Nilwala Ganga) | 5.40 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-11-11 21:01:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.46 | 🟡 Alert | -0.010 |  |
| 2026-11-11 21:03:26 | Thaldena (Mahaweli Ganga) | 2.20 | 🟢 Normal | 1.275 | 🔺 Rising |
| 2026-11-11 21:02:04 | Nawalapitiya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.680 | 🔺 Rising |
| 2026-11-11 21:08:39 | Katharagama (Menik Ganga) | 0.74 | 🟢 Normal | 0.624 | 🔺 Rising |
| 2026-11-11 22:01:26 | Wellawaya (Kirindi Oya) | 2.64 | 🟢 Normal | 0.487 | 🔺 Rising |
| 2026-11-11 21:02:44 | Nakkala (Kumbukkan Oya) | 1.66 | 🟢 Normal | 0.430 | 🔺 Rising |
| 2026-11-11 20:04:22 | Glencourse (Kelani Ganga) | 12.38 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-11-11 21:06:20 | Holombuwa (Kelani Ganga) | 2.40 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-11-11 21:00:22 | Pitabeddara (Nilwala Ganga) | 1.85 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-11-11 21:09:49 | Hanwella (Kelani Ganga) | 4.25 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-11-11 22:01:28 | Peradeniya (Mahaweli Ganga) | 4.75 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-11 21:01:45 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-11-11 21:10:33 | Rathnapura (Kalu Ganga) | 5.02 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-11 22:00:05 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-11 21:05:25 | Giriulla (Maha Oya) | 2.19 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-11 22:01:26 | Moragaswewa (Deduru Oya) | 3.65 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-11 22:02:11 | Thanamalwila (Kirindi Oya) | 2.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-11 21:09:14 | Badalgama (Maha Oya) | 3.45 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-11 18:01:56 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | 0.000 |  |
| 2026-11-11 18:01:41 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-11-11 21:05:32 | Ellagawa (Kalu Ganga) | 8.40 | 🟢 Normal | 0.000 |  |
| 2026-11-11 18:01:30 | Thanthirimale (Malwathu Oya) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-11-11 22:02:54 | Putupaula (Kalu Ganga) | 2.63 | 🟢 Normal | -0.010 |  |
| 2026-11-11 21:07:28 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | -0.020 |  |
| 2026-11-11 22:01:29 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | -0.025 |  |
| 2026-11-11 21:05:18 | Norwood (Kelani Ganga) | 1.33 | 🟢 Normal | -0.029 |  |
| 2026-11-11 21:03:02 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | -0.038 |  |
| 2026-11-11 21:02:11 | Manampitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.039 |  |
| 2026-11-11 22:01:31 | Kuda Oya (Kirindi Oya) | 2.11 | 🟢 Normal | -0.051 |  |
| 2026-11-11 22:01:27 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.063 |  |
| 2026-11-11 21:06:42 | Deraniyagala (Kelani Ganga) | 2.24 | 🟢 Normal | -0.419 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)