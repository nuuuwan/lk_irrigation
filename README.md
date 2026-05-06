# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--06_18:20:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **144,626 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-06 18:20:04 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:15:53 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:13:07 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:12:44 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.246 | 🔺 Rising |
| 2026-05-06 18:11:26 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:10:19 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:07:40 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.056 |  |
| 2026-05-06 18:07:37 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | -0.028 |  |
| 2026-05-06 18:07:19 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:07:09 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-05-06 18:06:41 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.020 |  |
| 2026-05-06 18:06:38 | Baddegama (Gin Ganga) | 0.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-06 18:05:43 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:05:19 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 18:04:56 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:04:51 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:04:42 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:04:39 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:04:05 | Manampitiya (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-06 18:04:03 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-05-06 18:03:25 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:03:12 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | -0.010 |  |
| 2026-05-06 18:03:07 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:02:55 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:02:41 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.021 |  |
| 2026-05-06 18:02:23 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-06 18:02:21 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.010 |  |
| 2026-05-06 18:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.030 |  |
| 2026-05-06 18:02:14 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-06 18:02:08 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-06 18:01:54 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:01:52 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:01:28 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-05-06 18:01:26 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-05-06 18:01:17 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:01:01 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-05-06 18:00:38 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-05-06 18:00:15 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | -0.041 |  |
| 2026-05-06 18:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 18:00:11 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-06 18:12:44 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.246 | 🔺 Rising |
| 2026-05-06 18:07:09 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-05-06 18:04:03 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-05-06 18:00:38 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-05-06 18:06:38 | Baddegama (Gin Ganga) | 0.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-06 18:02:08 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-06 18:04:05 | Manampitiya (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-06 18:02:23 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-06 18:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 18:00:11 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 18:05:19 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 18:01:52 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:04:56 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:01:17 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:02:55 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:07:19 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:20:04 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:04:51 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:01:54 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:11:26 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:15:53 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:05:43 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:03:07 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:10:19 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:04:39 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:03:25 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:13:07 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:02:21 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.010 |  |
| 2026-05-06 18:02:14 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-06 18:01:28 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-05-06 18:03:12 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | -0.010 |  |
| 2026-05-06 18:01:01 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-05-06 18:01:26 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-05-06 18:06:41 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.020 |  |
| 2026-05-06 18:02:41 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.021 |  |
| 2026-05-06 18:07:37 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | -0.028 |  |
| 2026-05-06 18:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.030 |  |
| 2026-05-06 18:00:15 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | -0.041 |  |
| 2026-05-06 18:07:40 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.056 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)