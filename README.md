# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--16_20:34:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **181,212 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-16 20:34:09 | Panadugama (Nilwala Ganga) | 3.26 | 🟢 Normal | -180.000 |  |
| 2026-06-16 20:34:07 | Panadugama (Nilwala Ganga) | 3.36 | 🟢 Normal | -180.000 |  |
| 2026-06-16 20:33:54 | Panadugama (Nilwala Ganga) | 3.36 | 🟢 Normal | -180.000 |  |
| 2026-06-16 20:25:13 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-06-16 20:19:30 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-16 20:17:48 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | -0.032 |  |
| 2026-06-16 20:12:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | -0.028 |  |
| 2026-06-16 20:11:55 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-16 20:09:17 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.071 |  |
| 2026-06-16 20:08:22 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-06-16 20:07:58 | Peradeniya (Mahaweli Ganga) | 1.84 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-06-16 20:05:25 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-06-16 20:04:34 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-16 20:04:33 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.087 |  |
| 2026-06-16 20:04:21 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-16 20:04:13 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.053 |  |
| 2026-06-16 20:04:04 | Putupaula (Kalu Ganga) | 1.08 | 🟢 Normal | -0.021 |  |
| 2026-06-16 20:04:01 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.030 |  |
| 2026-06-16 20:03:55 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-16 20:03:49 | Glencourse (Kelani Ganga) | 10.07 | 🟢 Normal | -0.079 |  |
| 2026-06-16 20:03:45 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-16 20:03:40 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-16 20:03:24 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-16 20:03:20 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.020 |  |
| 2026-06-16 20:03:18 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-16 20:03:11 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.021 |  |
| 2026-06-16 20:03:09 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-06-16 20:02:56 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-06-16 20:02:56 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-06-16 20:02:50 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-06-16 20:02:47 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-16 20:02:41 | Rathnapura (Kalu Ganga) | 1.73 | 🟢 Normal | -0.021 |  |
| 2026-06-16 20:02:36 | Hanwella (Kelani Ganga) | 2.12 | 🟢 Normal | -0.030 |  |
| 2026-06-16 20:02:24 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-16 20:02:11 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-16 20:01:57 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-06-16 20:01:57 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-16 20:01:48 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-16 20:01:18 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-16 20:01:17 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-16 20:07:58 | Peradeniya (Mahaweli Ganga) | 1.84 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-06-16 20:04:21 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-16 20:02:47 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-16 20:01:18 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-16 20:19:30 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-16 20:02:56 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-06-16 20:03:40 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-16 20:03:18 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-16 20:01:57 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:00:31 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-16 20:01:17 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-16 20:11:55 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-16 20:03:55 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-16 20:01:48 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-16 20:03:45 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-16 20:08:22 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-06-16 20:04:34 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:02:48 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-06-16 20:25:13 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-06-16 20:01:57 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-16 20:02:24 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-16 20:05:25 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-06-16 20:02:56 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-06-16 20:03:09 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-06-16 20:02:50 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-06-16 20:03:20 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.020 |  |
| 2026-06-16 20:02:41 | Rathnapura (Kalu Ganga) | 1.73 | 🟢 Normal | -0.021 |  |
| 2026-06-16 20:04:04 | Putupaula (Kalu Ganga) | 1.08 | 🟢 Normal | -0.021 |  |
| 2026-06-16 20:03:11 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.021 |  |
| 2026-06-16 20:12:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | -0.028 |  |
| 2026-06-16 20:04:01 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.030 |  |
| 2026-06-16 20:02:36 | Hanwella (Kelani Ganga) | 2.12 | 🟢 Normal | -0.030 |  |
| 2026-06-16 20:17:48 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | -0.032 |  |
| 2026-06-16 18:03:33 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.044 |  |
| 2026-06-16 20:04:13 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.053 |  |
| 2026-06-16 20:09:17 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.071 |  |
| 2026-06-16 20:03:49 | Glencourse (Kelani Ganga) | 10.07 | 🟢 Normal | -0.079 |  |
| 2026-06-16 20:04:33 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.087 |  |
| 2026-06-16 20:34:09 | Panadugama (Nilwala Ganga) | 3.26 | 🟢 Normal | -180.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)