# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--22_11:13:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **186,224 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-22 11:13:48 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-22 11:12:42 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 11:10:08 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-06-22 11:09:16 | Urawa (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-22 11:08:52 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-22 11:08:37 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-06-22 11:08:18 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-22 11:07:10 | Glencourse (Kelani Ganga) | 10.48 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-06-22 11:06:55 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-06-22 11:06:25 | Dunamale (Aththanagalu Oya) | 1.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-22 11:06:05 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-06-22 11:05:41 | Hanwella (Kelani Ganga) | 2.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-22 11:05:35 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-06-22 11:05:34 | Thanthirimale (Malwathu Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-06-22 11:05:26 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-06-22 11:05:25 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.095 |  |
| 2026-06-22 11:05:11 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-22 11:05:06 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-06-22 11:04:46 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-22 11:04:41 | Panadugama (Nilwala Ganga) | 3.28 | 🟢 Normal | 0.473 | 🔺 Rising |
| 2026-06-22 11:04:04 | Pitabeddara (Nilwala Ganga) | 1.29 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-22 11:03:49 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-22 11:03:47 | Magura (Kalu Ganga) | 2.65 | 🟢 Normal | 48.649 | 🔺 Rising |
| 2026-06-22 11:03:40 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.071 |  |
| 2026-06-22 11:03:12 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-22 11:03:04 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-06-22 11:02:33 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | 48.649 | 🔺 Rising |
| 2026-06-22 11:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.47 | 🟢 Normal | 0.309 | 🔺 Rising |
| 2026-06-22 11:02:09 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-22 11:01:43 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-22 11:01:19 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | 0.316 | 🔺 Rising |
| 2026-06-22 11:01:17 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-22 11:01:11 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-22 11:01:08 | Rathnapura (Kalu Ganga) | 1.90 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-06-22 11:01:03 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.021 |  |
| 2026-06-22 11:01:00 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 11:01:00 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-22 11:00:59 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-22 11:00:33 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.041 |  |
| 2026-06-22 11:00:25 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.046 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-22 11:03:47 | Magura (Kalu Ganga) | 2.65 | 🟢 Normal | 48.649 | 🔺 Rising |
| 2026-06-22 11:04:41 | Panadugama (Nilwala Ganga) | 3.28 | 🟢 Normal | 0.473 | 🔺 Rising |
| 2026-06-22 11:01:19 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | 0.316 | 🔺 Rising |
| 2026-06-22 11:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.47 | 🟢 Normal | 0.309 | 🔺 Rising |
| 2026-06-22 11:01:08 | Rathnapura (Kalu Ganga) | 1.90 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-06-22 11:07:10 | Glencourse (Kelani Ganga) | 10.48 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-06-22 11:06:55 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-06-22 11:05:35 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-06-22 11:09:16 | Urawa (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-22 11:08:37 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-06-22 11:05:41 | Hanwella (Kelani Ganga) | 2.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-22 11:04:04 | Pitabeddara (Nilwala Ganga) | 1.29 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-22 11:05:11 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-22 11:06:25 | Dunamale (Aththanagalu Oya) | 1.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-22 11:13:48 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-22 10:19:34 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-22 11:01:00 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 11:12:42 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 11:01:00 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-22 11:01:11 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-22 11:01:17 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-22 11:00:59 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-22 11:03:12 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-22 11:08:18 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-22 11:08:52 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-22 11:10:08 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-06-22 11:01:43 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-22 11:04:46 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-22 11:06:05 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-06-22 11:05:34 | Thanthirimale (Malwathu Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-06-22 11:05:06 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-06-22 11:03:49 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-22 11:02:09 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-22 11:03:04 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-06-22 11:01:03 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.021 |  |
| 2026-06-22 11:00:33 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.041 |  |
| 2026-06-22 11:00:25 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.046 |  |
| 2026-06-22 11:03:40 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.071 |  |
| 2026-06-22 11:05:25 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.095 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)