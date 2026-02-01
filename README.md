# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--01_06:17:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **61,289 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 06:17:28 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-01 06:12:50 | Manampitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-02-01 06:12:16 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-01 06:11:32 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-01 06:10:45 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.028 |  |
| 2026-02-01 06:10:19 | Panadugama (Nilwala Ganga) | 2.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-01 06:08:36 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | -0.004 |  |
| 2026-02-01 06:08:19 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-01 06:07:15 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-01 06:07:14 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.009 |  |
| 2026-02-01 06:05:50 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-01 06:05:28 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-01 06:05:13 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.357 |  |
| 2026-02-01 06:05:00 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.019 |  |
| 2026-02-01 06:04:58 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | -0.011 |  |
| 2026-02-01 06:04:03 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.308 | 🔺 Rising |
| 2026-02-01 06:04:02 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-01 06:03:59 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-01 06:03:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-02-01 06:03:42 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | -0.046 |  |
| 2026-02-01 06:03:24 | Padiyathalawa (Maduru Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 06:03:23 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 06:03:17 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-02-01 06:03:00 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.040 |  |
| 2026-02-01 06:02:53 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | -0.082 |  |
| 2026-02-01 06:02:50 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-01 06:02:27 | Dunamale (Aththanagalu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-01 06:02:25 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-01 06:02:23 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-01 06:02:16 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-01 06:01:29 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.032 |  |
| 2026-02-01 06:01:20 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-02-01 06:01:12 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 06:01:09 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.124 |  |
| 2026-02-01 06:01:00 | Rathnapura (Kalu Ganga) | 0.94 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-02-01 06:00:53 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 06:00:26 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 05:55:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-02-01 05:54:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-02-01 05:54:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.61 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-02-01 05:53:22 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:49:51 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-01 05:34:07 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.066 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 06:04:03 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.308 | 🔺 Rising |
| 2026-02-01 06:03:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-02-01 06:03:17 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-02-01 06:01:20 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-02-01 06:12:16 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-01 06:01:00 | Rathnapura (Kalu Ganga) | 0.94 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-02-01 06:10:19 | Panadugama (Nilwala Ganga) | 2.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-01 06:08:19 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-01 06:04:02 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-01 05:12:41 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 06:01:12 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 06:00:26 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 06:03:24 | Padiyathalawa (Maduru Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 06:05:28 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-01 06:03:23 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 06:02:25 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-01 06:07:15 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:08:19 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-01 06:11:32 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-01 06:17:28 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-01 06:02:50 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-01 06:02:27 | Dunamale (Aththanagalu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-01 06:02:16 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-01 06:03:59 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-01 06:02:23 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-01 06:12:50 | Manampitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:01:52 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-01 06:05:50 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-01 06:08:36 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | -0.004 |  |
| 2026-02-01 06:07:14 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.009 |  |
| 2026-02-01 06:04:58 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | -0.011 |  |
| 2026-02-01 06:05:00 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.019 |  |
| 2026-02-01 06:10:45 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.028 |  |
| 2026-02-01 06:01:29 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.032 |  |
| 2026-02-01 06:03:00 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.040 |  |
| 2026-02-01 06:03:42 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | -0.046 |  |
| 2026-02-01 06:02:53 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | -0.082 |  |
| 2026-02-01 06:01:09 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.124 |  |
| 2026-02-01 06:05:13 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.357 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)