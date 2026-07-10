# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--10_21:26:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **202,760 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-10 21:26:22 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-10 21:23:45 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.351 |  |
| 2026-07-10 21:15:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-07-10 21:12:29 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-10 21:11:04 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-10 21:10:44 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-10 21:08:01 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-10 21:07:39 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 21:06:13 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-07-10 21:06:04 | Glencourse (Kelani Ganga) | 10.00 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-10 21:05:34 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-10 21:05:29 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.087 |  |
| 2026-07-10 21:05:18 | Thalgahagoda (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.013 |  |
| 2026-07-10 21:05:08 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-10 21:04:54 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-10 21:04:48 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.087 |  |
| 2026-07-10 21:04:31 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-07-10 21:04:20 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-07-10 21:04:06 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 21:03:39 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-10 21:03:38 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-10 21:03:33 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-10 21:03:27 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-10 21:03:15 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-10 21:03:13 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-10 21:03:09 | Ellagawa (Kalu Ganga) | 4.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-10 21:03:05 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-10 21:02:52 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.100 |  |
| 2026-07-10 21:02:38 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-10 21:02:33 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-10 21:02:15 | Hanwella (Kelani Ganga) | 1.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-10 21:02:06 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-10 21:02:03 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-07-10 21:01:55 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.022 |  |
| 2026-07-10 21:01:41 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-10 21:01:33 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 21:01:31 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 21:01:20 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-10 21:00:42 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-10 21:04:31 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-07-10 21:06:04 | Glencourse (Kelani Ganga) | 10.00 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-10 21:03:33 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-10 21:03:09 | Ellagawa (Kalu Ganga) | 4.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-10 21:02:15 | Hanwella (Kelani Ganga) | 1.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-10 21:02:33 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-10 21:15:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-07-10 21:01:31 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 21:04:06 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 21:01:33 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 21:07:39 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 21:10:44 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-10 21:12:29 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-10 18:05:00 | Weraganthota (Mahaweli Ganga) | -3.43 | 🟢 Normal | 0.000 |  |
| 2026-07-10 21:02:06 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-10 21:04:54 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-10 21:02:38 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-10 21:01:41 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-10 21:01:20 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:09:34 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-10 21:11:04 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-10 21:03:27 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-10 21:26:22 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-10 21:03:38 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-10 21:03:05 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-10 21:05:08 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-10 21:06:13 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-07-10 21:03:15 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:01:40 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-10 21:03:13 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-10 21:08:01 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-10 21:05:34 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-10 21:02:03 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-07-10 21:05:18 | Thalgahagoda (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.013 |  |
| 2026-07-10 21:01:55 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.022 |  |
| 2026-07-10 21:05:29 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.087 |  |
| 2026-07-10 21:04:48 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.087 |  |
| 2026-07-10 21:02:52 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.100 |  |
| 2026-07-10 21:23:45 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.351 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)