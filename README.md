# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--18_14:59:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **155,253 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **10** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-18 14:59:21 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-05-18 14:14:16 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-05-18 14:10:57 | Thawalama (Gin Ganga) | 1.71 | 🟢 Normal | -0.009 |  |
| 2026-05-18 14:10:47 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | -0.018 |  |
| 2026-05-18 14:09:48 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | -0.019 |  |
| 2026-05-18 14:08:58 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-18 14:08:51 | Rathnapura (Kalu Ganga) | 1.91 | 🟢 Normal | -0.009 |  |
| 2026-05-18 14:08:05 | Thanthirimale (Malwathu Oya) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-05-18 14:07:52 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-18 14:07:38 | Ellagawa (Kalu Ganga) | 6.09 | 🟢 Normal | -0.028 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-18 14:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.54 | 🟡 Alert | -0.080 |  |
| 2026-05-18 14:01:11 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.240 | 🔺 Rising |
| 2026-05-18 14:07:03 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-18 14:07:27 | Moragaswewa (Deduru Oya) | 1.15 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-05-18 14:01:57 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-18 14:04:36 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-18 14:01:30 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-18 14:01:29 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-05-18 14:00:38 | Horowpothana (Yan Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-05-18 14:07:52 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-18 14:02:55 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-18 14:03:46 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-18 14:03:55 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-18 09:00:58 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-18 14:08:58 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-18 14:02:30 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-18 14:08:05 | Thanthirimale (Malwathu Oya) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-05-18 14:05:09 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-18 14:06:28 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-18 14:14:16 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-05-18 13:08:44 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-18 14:01:28 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-05-18 14:10:57 | Thawalama (Gin Ganga) | 1.71 | 🟢 Normal | -0.009 |  |
| 2026-05-18 14:08:51 | Rathnapura (Kalu Ganga) | 1.91 | 🟢 Normal | -0.009 |  |
| 2026-05-18 14:03:36 | Nawalapitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-05-18 14:01:37 | Galgamuwa (Mee Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-05-18 14:00:29 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-05-18 14:04:04 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | -0.011 |  |
| 2026-05-18 14:59:21 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-05-18 14:00:28 | Magura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.012 |  |
| 2026-05-18 14:10:47 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | -0.018 |  |
| 2026-05-18 14:09:48 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | -0.019 |  |
| 2026-05-18 14:00:28 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-05-18 14:07:38 | Ellagawa (Kalu Ganga) | 6.09 | 🟢 Normal | -0.028 |  |
| 2026-05-18 13:09:14 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | -0.030 |  |
| 2026-05-18 14:02:24 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.033 |  |
| 2026-05-18 14:03:32 | Putupaula (Kalu Ganga) | 1.90 | 🟢 Normal | -0.039 |  |
| 2026-05-18 14:02:23 | Glencourse (Kelani Ganga) | 9.96 | 🟢 Normal | -0.046 |  |
| 2026-05-18 14:03:22 | Hanwella (Kelani Ganga) | 2.22 | 🟢 Normal | -0.051 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)