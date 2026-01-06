# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--06_09:14:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **38,053 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 09:14:33 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.025 |  |
| 2026-01-06 09:13:15 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.022 |  |
| 2026-01-06 09:08:20 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-06 09:07:37 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.019 |  |
| 2026-01-06 09:06:48 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-06 09:06:13 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | -0.029 |  |
| 2026-01-06 09:06:09 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | 0.000 |  |
| 2026-01-06 09:05:42 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-06 09:05:30 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-06 09:05:30 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-06 09:05:09 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-06 09:04:48 | Thaldena (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-01-06 09:04:45 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.012 |  |
| 2026-01-06 09:04:16 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 09:03:53 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-01-06 09:03:48 | Weraganthota (Mahaweli Ganga) | -0.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-06 09:03:48 | Nakkala (Kumbukkan Oya) | 1.75 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-01-06 09:03:33 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-06 09:03:32 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-06 09:03:30 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.161 |  |
| 2026-01-06 09:03:24 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-01-06 09:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-01-06 09:02:53 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | -0.021 |  |
| 2026-01-06 09:02:50 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-06 09:02:44 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 09:02:44 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.011 |  |
| 2026-01-06 09:02:39 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-06 09:02:37 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-06 09:02:34 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-06 09:02:32 | Siyambalanduwa (Heda Oya) | 4.25 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-06 09:02:26 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.148 |  |
| 2026-01-06 09:01:45 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-01-06 09:01:43 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-01-06 09:01:23 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.367 | 🔺 Rising |
| 2026-01-06 09:01:15 | Padiyathalawa (Maduru Oya) | 2.35 | 🟢 Normal | -0.154 |  |
| 2026-01-06 09:01:10 | Yaka Wewa (Ma Oya) | 1.18 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-01-06 09:00:49 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-01-06 09:00:20 | Manampitiya (Mahaweli Ganga) | 3.10 | 🟡 Alert | 0.155 | 🔺 Rising |
| 2026-01-06 08:27:22 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.025 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 09:00:20 | Manampitiya (Mahaweli Ganga) | 3.10 | 🟡 Alert | 0.155 | 🔺 Rising |
| 2026-01-06 09:01:23 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.367 | 🔺 Rising |
| 2026-01-06 09:03:48 | Nakkala (Kumbukkan Oya) | 1.75 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-01-06 09:01:43 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-01-06 09:01:10 | Yaka Wewa (Ma Oya) | 1.18 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-01-06 09:04:48 | Thaldena (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-01-06 09:01:45 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-01-06 09:02:32 | Siyambalanduwa (Heda Oya) | 4.25 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-06 09:03:33 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-06 09:02:39 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-06 09:03:48 | Weraganthota (Mahaweli Ganga) | -0.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-06 09:06:48 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-06 09:02:44 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 09:04:16 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 09:03:53 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-01-06 09:02:37 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-06 09:02:34 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-06 09:05:42 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-06 09:05:30 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-06 09:06:09 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | 0.000 |  |
| 2026-01-06 09:03:32 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-06 09:08:20 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-06 09:05:30 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-06 09:05:09 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-06 09:02:50 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-06 09:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-01-06 09:03:24 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-01-06 09:00:49 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-01-06 09:02:44 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.011 |  |
| 2026-01-06 09:04:45 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.012 |  |
| 2026-01-06 08:08:44 | Panadugama (Nilwala Ganga) | 2.97 | 🟢 Normal | -0.016 |  |
| 2026-01-06 09:07:37 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.019 |  |
| 2026-01-06 09:02:53 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | -0.021 |  |
| 2026-01-06 09:13:15 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.022 |  |
| 2026-01-06 09:14:33 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.025 |  |
| 2026-01-06 09:06:13 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | -0.029 |  |
| 2026-01-06 09:02:26 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.148 |  |
| 2026-01-06 09:01:15 | Padiyathalawa (Maduru Oya) | 2.35 | 🟢 Normal | -0.154 |  |
| 2026-01-06 09:03:30 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.161 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)