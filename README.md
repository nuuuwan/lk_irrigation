# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--20_16:12:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **211,483 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-20 16:12:47 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:12:38 | Thalgahagoda (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.063 |  |
| 2026-07-20 16:11:23 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-20 16:09:35 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | -0.009 |  |
| 2026-07-20 16:07:56 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | -0.009 |  |
| 2026-07-20 16:07:38 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:07:37 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.009 |  |
| 2026-07-20 16:07:36 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:07:04 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-07-20 16:06:53 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -0.019 |  |
| 2026-07-20 16:06:17 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:06:05 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:05:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-07-20 16:05:38 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:05:10 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:04:53 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-20 16:04:35 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-20 16:04:14 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-07-20 16:04:13 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:04:02 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.362 | 🔺 Rising |
| 2026-07-20 16:03:42 | Thanthirimale (Malwathu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:03:41 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:03:33 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:03:08 | Glencourse (Kelani Ganga) | 9.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-20 16:03:08 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-07-20 16:02:59 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-07-20 16:02:42 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:02:39 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:02:29 | Thanamalwila (Kirindi Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:02:27 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:02:25 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:01:53 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:01:51 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:01:34 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:01:33 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:01:33 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:00:45 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.030 |  |
| 2026-07-20 16:00:39 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.020 |  |
| 2026-07-20 16:00:10 | Nakkala (Kumbukkan Oya) | 0.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-20 16:04:02 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.362 | 🔺 Rising |
| 2026-07-20 16:03:08 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-07-20 16:02:59 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-07-20 16:04:53 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-20 16:03:08 | Glencourse (Kelani Ganga) | 9.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-20 16:04:35 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-20 16:11:23 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-20 16:02:27 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:00:10 | Nakkala (Kumbukkan Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:01:34 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:02:39 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:01:51 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:07:36 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:07:38 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:03:33 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:01:33 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:01:53 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:12:47 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:04:13 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:06:05 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:01:33 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:05:38 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:06:17 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:02:42 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:03:42 | Thanthirimale (Malwathu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:03:41 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-20 15:05:04 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:02:25 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:02:29 | Thanamalwila (Kirindi Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-20 16:09:35 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | -0.009 |  |
| 2026-07-20 16:07:56 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | -0.009 |  |
| 2026-07-20 16:07:37 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.009 |  |
| 2026-07-20 16:05:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-07-20 16:04:14 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-07-20 16:06:53 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -0.019 |  |
| 2026-07-20 16:07:04 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-07-20 16:00:39 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.020 |  |
| 2026-07-20 16:00:45 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.030 |  |
| 2026-07-20 16:12:38 | Thalgahagoda (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.063 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)