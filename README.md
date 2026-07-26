# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--26_16:12:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **216,875 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-26 16:12:08 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.009 |  |
| 2026-07-26 16:10:23 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-26 16:09:34 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:09:26 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:08:51 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:08:33 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:06:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:06:31 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:06:21 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.030 |  |
| 2026-07-26 16:05:14 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:04:38 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:03:55 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-26 16:03:52 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-07-26 16:03:49 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.038 |  |
| 2026-07-26 16:03:35 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.048 |  |
| 2026-07-26 16:03:31 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:03:29 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.049 |  |
| 2026-07-26 16:03:26 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:03:11 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.062 |  |
| 2026-07-26 16:02:59 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:02:33 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-26 16:02:17 | Thanamalwila (Kirindi Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:02:15 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:02:00 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:01:50 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-07-26 16:01:48 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-07-26 16:01:45 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:01:40 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-07-26 16:01:37 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:01:34 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:01:25 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:01:21 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:01:19 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:01:17 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:01:17 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-26 16:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:01:11 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-26 16:01:40 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-07-26 16:03:52 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-07-26 16:03:55 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-26 16:02:33 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-26 16:01:50 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-07-26 16:01:17 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-26 16:10:23 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-26 16:02:15 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:01:11 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:09:34 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:01:19 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:04:38 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-26 15:00:45 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:01:17 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:06:31 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:03:31 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:02:59 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:08:33 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:03:26 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:01:34 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:01:37 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:01:21 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:01:45 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:08:51 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:05:14 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:01:25 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:09:26 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:02:00 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:02:17 | Thanamalwila (Kirindi Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:06:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-07-26 16:12:08 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.009 |  |
| 2026-07-26 16:01:48 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-07-26 15:03:23 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.011 |  |
| 2026-07-26 16:06:21 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.030 |  |
| 2026-07-26 16:03:49 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.038 |  |
| 2026-07-26 16:03:35 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.048 |  |
| 2026-07-26 16:03:29 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.049 |  |
| 2026-07-26 16:03:11 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.062 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)