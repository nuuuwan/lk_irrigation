# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--04_14:02:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **170,268 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 14:02:29 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-04 14:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.18 | 🟢 Normal | -0.041 |  |
| 2026-06-04 14:02:14 | Dunamale (Aththanagalu Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-06-04 14:02:11 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 14:02:09 | Nawalapitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 14:02:09 | Deraniyagala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-06-04 14:02:04 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-06-04 14:02:02 | Baddegama (Gin Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-06-04 14:01:44 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-04 14:01:24 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-04 14:01:17 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-04 14:01:17 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.006 |  |
| 2026-06-04 14:01:12 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-04 14:01:10 | Ellagawa (Kalu Ganga) | 6.36 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-04 14:00:52 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-06-04 14:00:39 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-04 14:00:12 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-04 14:00:10 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.010 |  |
| 2026-06-04 14:00:09 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 13:56:51 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-04 13:14:51 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-04 13:14:43 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.039 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 14:02:09 | Deraniyagala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-06-04 13:02:21 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-06-04 13:06:35 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-06-04 13:04:01 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-06-04 13:00:18 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-04 14:01:17 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-04 14:01:10 | Ellagawa (Kalu Ganga) | 6.36 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-04 13:14:43 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-04 13:08:29 | Rathnapura (Kalu Ganga) | 2.58 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-04 14:01:12 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-04 13:05:01 | Hanwella (Kelani Ganga) | 2.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-04 13:01:45 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-06-04 13:06:44 | Panadugama (Nilwala Ganga) | 2.86 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-06-04 13:05:54 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-04 13:14:51 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-04 14:02:29 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-04 13:03:34 | Moragaswewa (Deduru Oya) | 0.32 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-04 13:07:00 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 14:02:09 | Nawalapitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 13:07:19 | Glencourse (Kelani Ganga) | 10.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 14:01:24 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-04 14:00:09 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 14:01:44 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-04 14:02:11 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 13:04:47 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-04 14:02:04 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-06-04 14:02:02 | Baddegama (Gin Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-06-04 13:06:45 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-04 13:02:00 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-04 13:02:38 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-04 14:02:14 | Dunamale (Aththanagalu Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-06-04 13:02:03 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-04 13:03:14 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-04 14:00:39 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-04 14:00:52 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-06-04 14:00:12 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-04 14:01:17 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.006 |  |
| 2026-06-04 14:00:10 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.010 |  |
| 2026-06-04 14:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.18 | 🟢 Normal | -0.041 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)