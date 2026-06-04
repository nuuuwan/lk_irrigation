# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--04_06:36:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **169,970 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **8** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 06:36:16 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-04 06:13:33 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-06-04 06:10:51 | Dunamale (Aththanagalu Oya) | 1.32 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-04 06:10:29 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | 9.600 | 🔺 Rising |
| 2026-06-04 06:10:14 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | 9.600 | 🔺 Rising |
| 2026-06-04 06:09:23 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-04 06:09:13 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-04 06:08:42 | Rathnapura (Kalu Ganga) | 2.57 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 06:10:29 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | 9.600 | 🔺 Rising |
| 2026-06-04 06:04:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.10 | 🟢 Normal | 1.038 | 🔺 Rising |
| 2026-06-04 06:00:36 | Magura (Kalu Ganga) | 1.83 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2026-06-04 06:01:53 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-06-04 06:07:14 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-06-04 06:05:38 | Hanwella (Kelani Ganga) | 2.06 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-06-04 06:08:02 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-04 06:03:37 | Glencourse (Kelani Ganga) | 10.63 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-06-04 06:00:09 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-04 06:01:07 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-04 06:03:14 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-04 06:10:51 | Dunamale (Aththanagalu Oya) | 1.32 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-04 06:00:21 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-06-04 06:01:41 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-04 06:07:57 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-04 06:00:20 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-04 06:01:35 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 06:00:33 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 06:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-06-04 06:01:33 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-04 06:04:30 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-04 06:36:16 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:03:16 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-04 06:02:55 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-04 06:02:35 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-04 06:02:32 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-04 06:06:07 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-04 06:00:55 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:01:27 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-04 06:09:23 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-04 06:09:13 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-04 06:08:42 | Rathnapura (Kalu Ganga) | 2.57 | 🟢 Normal | -0.010 |  |
| 2026-06-04 06:13:33 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-06-04 06:01:17 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.011 |  |
| 2026-06-04 06:07:37 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.018 |  |
| 2026-06-04 06:06:27 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-06-04 06:06:13 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.041 |  |
| 2026-06-04 06:06:02 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.103 |  |
| 2026-06-04 06:03:46 | Deraniyagala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.190 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)