# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--10_05:17:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **41,496 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **46** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 05:17:09 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-10 05:16:59 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-10 05:15:42 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-10 05:14:22 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-10 05:13:02 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | -0.021 |  |
| 2026-01-10 05:11:57 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | -0.017 |  |
| 2026-01-10 05:11:11 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-01-10 05:10:43 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | -0.019 |  |
| 2026-01-10 05:08:50 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.013 |  |
| 2026-01-10 05:08:30 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-01-10 05:07:46 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-10 05:07:15 | Thanamalwila (Kirindi Oya) | 1.31 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-01-10 05:05:48 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-10 05:05:47 | Baddegama (Gin Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-01-10 05:05:21 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-10 05:05:02 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-10 05:04:13 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-10 05:04:02 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-01-10 05:04:01 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 05:03:57 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.019 |  |
| 2026-01-10 05:03:53 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-10 05:03:31 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-01-10 05:03:19 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -7.200 |  |
| 2026-01-10 05:03:03 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.202 |  |
| 2026-01-10 05:02:59 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -7.200 |  |
| 2026-01-10 05:02:55 | Thaldena (Mahaweli Ganga) | 0.91 | 🟢 Normal | -36.000 |  |
| 2026-01-10 05:02:54 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | -36.000 |  |
| 2026-01-10 05:02:53 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | -36.000 |  |
| 2026-01-10 05:02:52 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | -36.000 |  |
| 2026-01-10 05:02:50 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | -36.000 |  |
| 2026-01-10 05:02:37 | Katharagama (Menik Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-10 05:02:29 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | -0.004 |  |
| 2026-01-10 05:02:20 | Horowpothana (Yan Oya) | 2.49 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-10 05:02:18 | Yaka Wewa (Ma Oya) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 05:02:10 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-10 05:02:03 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-10 05:01:37 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 05:01:26 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-10 05:01:08 | Moragaswewa (Deduru Oya) | 1.02 | 🟢 Normal | -0.015 |  |
| 2026-01-10 04:56:07 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 04:39:52 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | -0.019 |  |
| 2026-01-10 04:32:17 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-10 04:30:06 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-10 04:28:31 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-01-10 04:23:34 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.013 |  |
| 2026-01-10 04:20:44 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.036 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 04:06:33 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 13.846 | 🔺 Rising |
| 2026-01-10 05:03:31 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-01-10 05:07:15 | Thanamalwila (Kirindi Oya) | 1.31 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-01-10 05:17:09 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-10 05:02:20 | Horowpothana (Yan Oya) | 2.49 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-10 05:11:11 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-01-10 02:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-10 05:01:26 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-10 05:02:10 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-10 05:07:46 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 17:13:03 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-10 03:08:22 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-10 05:16:59 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-10 05:04:01 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 05:02:18 | Yaka Wewa (Ma Oya) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 05:03:53 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-10 05:14:22 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-10 05:15:42 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-10 05:02:03 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-10 05:08:30 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-01-10 05:05:21 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-10 05:01:37 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 05:02:37 | Katharagama (Menik Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-10 05:05:02 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-10 05:04:13 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-10 05:02:29 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | -0.004 |  |
| 2026-01-10 05:04:02 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-01-10 05:05:47 | Baddegama (Gin Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-01-09 18:00:08 | Weraganthota (Mahaweli Ganga) | -1.21 | 🟢 Normal | -0.010 |  |
| 2026-01-09 18:08:00 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-01-10 05:08:50 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.013 |  |
| 2026-01-10 05:01:08 | Moragaswewa (Deduru Oya) | 1.02 | 🟢 Normal | -0.015 |  |
| 2026-01-10 05:11:57 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | -0.017 |  |
| 2026-01-10 05:03:57 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.019 |  |
| 2026-01-10 05:10:43 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | -0.019 |  |
| 2026-01-10 05:13:02 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | -0.021 |  |
| 2026-01-10 05:03:03 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.202 |  |
| 2026-01-10 05:03:19 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -7.200 |  |
| 2026-01-10 05:02:55 | Thaldena (Mahaweli Ganga) | 0.91 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)