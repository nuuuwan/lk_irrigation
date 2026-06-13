# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--13_15:05:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **178,344 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 15:05:34 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-13 15:05:34 | Deraniyagala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-06-13 15:05:06 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-13 15:04:54 | Dunamale (Aththanagalu Oya) | 3.30 | 🟡 Alert | -0.019 |  |
| 2026-06-13 15:04:44 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-06-13 15:04:37 | Thawalama (Gin Ganga) | 2.55 | 🟢 Normal | -0.049 |  |
| 2026-06-13 15:04:18 | Glencourse (Kelani Ganga) | 11.82 | 🟢 Normal | -0.030 |  |
| 2026-06-13 15:03:53 | Putupaula (Kalu Ganga) | 2.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-13 15:03:52 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | -0.029 |  |
| 2026-06-13 15:03:27 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-06-13 15:03:26 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-13 15:03:25 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-13 15:03:02 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.019 |  |
| 2026-06-13 15:02:52 | Moragaswewa (Deduru Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-13 15:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.50 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-06-13 15:02:33 | Rathnapura (Kalu Ganga) | 5.21 | 🟡 Alert | -0.063 |  |
| 2026-06-13 15:02:27 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-06-13 15:02:12 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-06-13 15:02:11 | Magura (Kalu Ganga) | 4.05 | 🟡 Alert | -0.015 |  |
| 2026-06-13 15:02:09 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.010 |  |
| 2026-06-13 15:01:54 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-06-13 15:01:49 | Giriulla (Maha Oya) | 2.37 | 🟢 Normal | -0.010 |  |
| 2026-06-13 15:01:46 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-13 15:01:46 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-13 15:01:44 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-13 15:01:19 | Ellagawa (Kalu Ganga) | 8.65 | 🟢 Normal | 0.000 |  |
| 2026-06-13 15:01:15 | Holombuwa (Kelani Ganga) | 1.34 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-13 15:01:11 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | -0.033 |  |
| 2026-06-13 15:00:13 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-13 14:15:42 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 15:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.50 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-06-13 15:02:11 | Magura (Kalu Ganga) | 4.05 | 🟡 Alert | -0.015 |  |
| 2026-06-13 15:04:54 | Dunamale (Aththanagalu Oya) | 3.30 | 🟡 Alert | -0.019 |  |
| 2026-06-13 15:02:33 | Rathnapura (Kalu Ganga) | 5.21 | 🟡 Alert | -0.063 |  |
| 2026-06-13 15:05:34 | Deraniyagala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-06-13 15:01:44 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-13 15:05:34 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-13 15:01:15 | Holombuwa (Kelani Ganga) | 1.34 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-13 14:01:07 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-13 15:03:53 | Putupaula (Kalu Ganga) | 2.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-13 14:00:56 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 15:02:52 | Moragaswewa (Deduru Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-13 15:01:54 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-06-13 15:01:46 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-13 15:03:26 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-13 15:02:27 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-06-13 15:01:19 | Ellagawa (Kalu Ganga) | 8.65 | 🟢 Normal | 0.000 |  |
| 2026-06-13 14:07:42 | Baddegama (Gin Ganga) | 3.19 | 🟢 Normal | 0.000 |  |
| 2026-06-13 15:05:06 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-13 15:03:25 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-13 15:01:46 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-13 14:02:44 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-06-13 15:00:13 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-13 14:05:58 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-06-13 15:01:49 | Giriulla (Maha Oya) | 2.37 | 🟢 Normal | -0.010 |  |
| 2026-06-13 15:04:44 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-06-13 15:02:09 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.010 |  |
| 2026-06-13 14:06:52 | Badalgama (Maha Oya) | 3.48 | 🟢 Normal | -0.010 |  |
| 2026-06-13 15:03:27 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-06-13 15:03:02 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.019 |  |
| 2026-06-13 15:02:12 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-06-13 14:05:21 | Peradeniya (Mahaweli Ganga) | 2.35 | 🟢 Normal | -0.020 |  |
| 2026-06-13 14:02:13 | Galgamuwa (Mee Oya) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-06-13 15:03:52 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | -0.029 |  |
| 2026-06-13 15:04:18 | Glencourse (Kelani Ganga) | 11.82 | 🟢 Normal | -0.030 |  |
| 2026-06-13 15:01:11 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | -0.033 |  |
| 2026-06-13 14:12:42 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.036 |  |
| 2026-06-13 14:03:43 | Panadugama (Nilwala Ganga) | 4.48 | 🟢 Normal | -0.043 |  |
| 2026-06-13 15:04:37 | Thawalama (Gin Ganga) | 2.55 | 🟢 Normal | -0.049 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)