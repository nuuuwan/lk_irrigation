# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--09_09:13:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **201,391 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-09 09:13:08 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | -0.009 |  |
| 2026-07-09 09:09:17 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:08:16 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:07:46 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:07:14 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:06:02 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:05:42 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-07-09 09:05:41 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:05:27 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:05:16 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:05:04 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:04:58 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:04:38 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:04:19 | Glencourse (Kelani Ganga) | 9.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-09 09:04:16 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.029 |  |
| 2026-07-09 09:04:16 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-09 09:03:53 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-07-09 09:03:39 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:03:28 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:03:23 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-09 09:03:16 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-07-09 09:03:01 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:02:57 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-09 09:02:49 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-09 09:02:40 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-09 09:02:39 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:02:36 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-09 09:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.050 |  |
| 2026-07-09 09:02:31 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:01:39 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:01:37 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.240 | 🔺 Rising |
| 2026-07-09 09:01:33 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:01:30 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:01:28 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | -0.053 |  |
| 2026-07-09 09:01:26 | Ellagawa (Kalu Ganga) | 4.48 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:01:25 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-09 09:01:15 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:00:58 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:00:28 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:00:12 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-09 09:01:37 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.240 | 🔺 Rising |
| 2026-07-09 09:01:25 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-09 09:00:12 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-09 09:02:36 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-09 09:02:49 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-09 09:04:16 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-09 09:03:23 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-09 09:02:57 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-09 09:04:19 | Glencourse (Kelani Ganga) | 9.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-09 09:02:40 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-09 09:02:31 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:00:58 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:01:33 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:01:39 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:03:01 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:07:46 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:04:38 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:01:15 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:05:27 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:01:26 | Ellagawa (Kalu Ganga) | 4.48 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:04:58 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:03:28 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:05:16 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:09:17 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:02:39 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:06:02 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:01:30 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:07:14 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:00:28 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:05:41 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:05:04 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-09 09:13:08 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | -0.009 |  |
| 2026-07-09 09:03:53 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-07-09 09:03:16 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-07-09 09:05:42 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-07-09 08:04:35 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.021 |  |
| 2026-07-09 09:04:16 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.029 |  |
| 2026-07-09 09:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.050 |  |
| 2026-07-09 09:01:28 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | -0.053 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)