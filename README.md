# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--12_20:17:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **286,147 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Norwood — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 20:17:08 | Magura (Kalu Ganga) | 2.65 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-10-12 20:08:50 | Rathnapura (Kalu Ganga) | 2.75 | 🟢 Normal | 0.265 | 🔺 Rising |
| 2026-10-12 20:07:01 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-12 20:06:58 | Thawalama (Gin Ganga) | 2.95 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-10-12 20:06:52 | Putupaula (Kalu Ganga) | 1.79 | 🟢 Normal | -0.053 |  |
| 2026-10-12 20:06:43 | Norwood (Kelani Ganga) | 1.61 | 🟡 Alert | -0.328 |  |
| 2026-10-12 20:06:26 | Urawa (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.890 | 🔺 Rising |
| 2026-10-12 20:05:25 | Pitabeddara (Nilwala Ganga) | 1.56 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-10-12 20:05:13 | Baddegama (Gin Ganga) | 2.49 | 🟢 Normal | -0.040 |  |
| 2026-10-12 20:04:59 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 20:04:47 | Dunamale (Aththanagalu Oya) | 2.43 | 🟢 Normal | -0.019 |  |
| 2026-10-12 20:04:41 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-10-12 20:04:35 | Ellagawa (Kalu Ganga) | 6.83 | 🟢 Normal | -0.010 |  |
| 2026-10-12 20:04:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-10-12 20:04:31 | Panadugama (Nilwala Ganga) | 5.22 | 🟡 Alert | 1.234 | 🔺 Rising |
| 2026-10-12 20:04:10 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-12 20:04:06 | Badalgama (Maha Oya) | 3.13 | 🟢 Normal | -0.040 |  |
| 2026-10-12 20:03:56 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.213 |  |
| 2026-10-12 20:03:30 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-12 20:03:20 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-12 20:03:15 | Moragaswewa (Deduru Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-12 20:03:07 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.082 |  |
| 2026-10-12 20:02:51 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.011 |  |
| 2026-10-12 20:02:34 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-12 20:02:29 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-12 20:02:17 | Giriulla (Maha Oya) | 1.79 | 🟢 Normal | -0.021 |  |
| 2026-10-12 20:02:17 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-12 20:02:17 | Hanwella (Kelani Ganga) | 3.64 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-10-12 20:01:57 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-12 20:01:40 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-12 20:01:29 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-12 20:01:19 | Glencourse (Kelani Ganga) | 11.68 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-10-12 20:01:15 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-12 20:01:10 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-12 19:52:51 | Panadugama (Nilwala Ganga) | 4.98 | 🟢 Normal | 1.234 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 20:04:31 | Panadugama (Nilwala Ganga) | 5.22 | 🟡 Alert | 1.234 | 🔺 Rising |
| 2026-10-12 20:04:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-10-12 20:06:43 | Norwood (Kelani Ganga) | 1.61 | 🟡 Alert | -0.328 |  |
| 2026-10-12 20:06:26 | Urawa (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.890 | 🔺 Rising |
| 2026-10-12 20:08:50 | Rathnapura (Kalu Ganga) | 2.75 | 🟢 Normal | 0.265 | 🔺 Rising |
| 2026-10-12 20:06:58 | Thawalama (Gin Ganga) | 2.95 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-10-12 20:02:17 | Hanwella (Kelani Ganga) | 3.64 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-10-12 20:04:10 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-12 20:17:08 | Magura (Kalu Ganga) | 2.65 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-10-12 20:05:25 | Pitabeddara (Nilwala Ganga) | 1.56 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-10-12 20:02:29 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-12 20:01:19 | Glencourse (Kelani Ganga) | 11.68 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-10-12 20:03:30 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-12 20:01:57 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-12 20:07:01 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-12 20:04:59 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 18:02:58 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | 0.000 |  |
| 2026-10-12 20:03:20 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-12 20:01:15 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-12 20:03:15 | Moragaswewa (Deduru Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-12 20:01:40 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-12 19:01:11 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:02:38 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-12 19:19:52 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-12 20:02:34 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-12 20:01:10 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-12 20:01:29 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:01:38 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-12 20:02:17 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-12 20:04:35 | Ellagawa (Kalu Ganga) | 6.83 | 🟢 Normal | -0.010 |  |
| 2026-10-12 20:04:41 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-10-12 20:02:51 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.011 |  |
| 2026-10-12 20:04:47 | Dunamale (Aththanagalu Oya) | 2.43 | 🟢 Normal | -0.019 |  |
| 2026-10-12 20:02:17 | Giriulla (Maha Oya) | 1.79 | 🟢 Normal | -0.021 |  |
| 2026-10-12 20:04:06 | Badalgama (Maha Oya) | 3.13 | 🟢 Normal | -0.040 |  |
| 2026-10-12 20:05:13 | Baddegama (Gin Ganga) | 2.49 | 🟢 Normal | -0.040 |  |
| 2026-10-12 20:06:52 | Putupaula (Kalu Ganga) | 1.79 | 🟢 Normal | -0.053 |  |
| 2026-10-12 20:03:07 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.082 |  |
| 2026-10-12 20:03:56 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.213 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)