# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--15_03:23:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **206,530 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-15 03:23:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-07-15 03:21:49 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:13:05 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.009 |  |
| 2026-07-15 03:11:24 | Baddegama (Gin Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-07-15 03:08:11 | Glencourse (Kelani Ganga) | 9.21 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:08:04 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-15 03:07:55 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:06:12 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:05:26 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-07-15 03:05:22 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:05:17 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:04:59 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:04:49 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.020 |  |
| 2026-07-15 03:04:22 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:03:55 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:03:39 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:03:33 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2026-07-15 03:03:23 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:03:09 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:03:09 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:03:02 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:02:46 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:02:37 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:02:36 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:02:33 | Thanamalwila (Kirindi Oya) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-07-15 03:02:13 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:01:59 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:01:52 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:01:52 | Siyambalanduwa (Heda Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:01:48 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-15 03:01:45 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-07-15 03:01:14 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:00:47 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-15 02:56:20 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-15 02:49:09 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-15 02:16:11 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-07-14 18:02:37 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-07-15 03:23:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-07-15 03:01:45 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-07-15 03:08:04 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-15 03:01:48 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-15 03:02:37 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:01:52 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:00:47 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:01:59 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:07:55 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:02:46 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:03:09 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:02:13 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-14 18:03:13 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:04:59 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:03:55 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:05:22 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | 0.000 |  |
| 2026-07-15 02:02:32 | Panadugama (Nilwala Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:02:36 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:08:11 | Glencourse (Kelani Ganga) | 9.21 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:03:09 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:01:52 | Siyambalanduwa (Heda Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:03:02 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:01:14 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:06:12 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:03:39 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-14 18:01:22 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:05:17 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-07-15 02:03:46 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:21:49 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:03:23 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-15 03:13:05 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.009 |  |
| 2026-07-15 03:02:33 | Thanamalwila (Kirindi Oya) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-07-15 03:05:26 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-07-15 03:11:24 | Baddegama (Gin Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-07-15 03:04:49 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.020 |  |
| 2026-07-15 03:03:33 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2026-07-15 02:03:08 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -1.241 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)