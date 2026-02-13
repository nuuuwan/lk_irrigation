# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--14_02:19:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **72,436 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 02:19:35 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-14 02:18:26 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-14 02:18:05 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-14 02:17:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-14 02:16:51 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-14 02:16:50 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-14 02:16:48 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-14 02:16:47 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-14 02:08:51 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-02-14 02:07:42 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -1.714 |  |
| 2026-02-14 02:07:00 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -1.714 |  |
| 2026-02-14 02:06:34 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | -1.091 |  |
| 2026-02-14 02:06:11 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.742 |  |
| 2026-02-14 02:06:01 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | -1.091 |  |
| 2026-02-14 02:05:51 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.021 |  |
| 2026-02-14 02:05:32 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-14 02:05:13 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-14 02:04:53 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-14 02:04:40 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-14 02:04:34 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.742 |  |
| 2026-02-14 02:03:56 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-02-14 02:03:25 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-02-14 02:03:08 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -324.000 |  |
| 2026-02-14 02:03:07 | Peradeniya (Mahaweli Ganga) | 2.14 | 🟢 Normal | -324.000 |  |
| 2026-02-14 02:02:36 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-14 02:02:32 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-14 02:02:31 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.005 |  |
| 2026-02-14 02:02:03 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-14 02:01:52 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 02:01:50 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-14 02:01:44 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-14 02:01:37 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-14 02:01:15 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | -0.040 |  |
| 2026-02-14 02:01:05 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-02-14 02:00:59 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-14 01:39:51 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-02-14 01:37:11 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 02:08:51 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-02-14 01:08:28 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-02-14 02:17:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-14 02:00:59 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-14 02:05:13 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-14 02:01:52 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 01:39:51 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-02-14 02:01:50 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-14 02:01:44 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-14 02:02:36 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-14 02:19:35 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-14 01:03:02 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-14 02:02:32 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:00:50 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-14 02:16:51 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-14 02:04:40 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-14 00:05:04 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-02-14 02:02:03 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-14 01:03:33 | Dunamale (Aththanagalu Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-14 02:05:32 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-14 02:01:05 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-02-14 02:04:53 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-14 01:27:21 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:03:07 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-14 01:17:35 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-14 01:37:11 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-14 01:25:54 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-14 02:02:31 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.005 |  |
| 2026-02-14 02:03:56 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-02-14 01:00:26 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-02-14 02:05:51 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.021 |  |
| 2026-02-14 02:03:25 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-02-14 02:01:15 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | -0.040 |  |
| 2026-02-13 18:01:13 | Weraganthota (Mahaweli Ganga) | -2.42 | 🟢 Normal | -0.050 |  |
| 2026-02-14 02:06:11 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.742 |  |
| 2026-02-14 02:06:34 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | -1.091 |  |
| 2026-02-14 01:02:40 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -1.161 |  |
| 2026-02-14 02:07:42 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -1.714 |  |
| 2026-02-14 02:03:08 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -324.000 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)