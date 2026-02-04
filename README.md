# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--04_16:14:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **64,121 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-04 16:14:31 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | -0.008 |  |
| 2026-02-04 16:11:37 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | -0.009 |  |
| 2026-02-04 16:09:38 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.045 |  |
| 2026-02-04 16:06:52 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-04 16:06:48 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-04 16:06:39 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-04 16:05:47 | Baddegama (Gin Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-02-04 16:05:29 | Weraganthota (Mahaweli Ganga) | -2.47 | 🟢 Normal | -0.046 |  |
| 2026-02-04 16:05:25 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-04 16:04:28 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-02-04 16:04:27 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-02-04 16:04:22 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.029 |  |
| 2026-02-04 16:03:55 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-04 16:03:50 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-02-04 16:03:43 | Dunamale (Aththanagalu Oya) | 0.28 | 🟢 Normal | -0.019 |  |
| 2026-02-04 16:03:33 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-02-04 16:03:25 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-04 16:03:11 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-04 16:03:03 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-04 16:03:01 | Glencourse (Kelani Ganga) | 8.49 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-04 16:03:00 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | -0.019 |  |
| 2026-02-04 16:02:57 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-04 16:02:32 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-04 16:02:31 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-04 16:02:04 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-04 16:01:51 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-04 16:01:49 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-02-04 16:01:21 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-04 16:01:19 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-04 16:00:06 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-04 15:59:42 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-04 16:01:49 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-04 16:04:27 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-02-04 16:03:33 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-02-04 16:01:21 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-04 16:03:01 | Glencourse (Kelani Ganga) | 8.49 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-04 16:03:03 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-04 16:03:55 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-04 16:01:51 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-04 16:02:04 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-04 16:02:57 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-04 16:03:25 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-04 16:06:48 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09⌛ | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-04 16:01:19 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-04 16:02:31 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-04 16:03:11 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-04 16:00:06 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-04 16:05:25 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-04 16:03:50 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-02-04 16:06:52 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-04 16:02:32 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-04 16:06:39 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-04 16:14:31 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | -0.008 |  |
| 2026-02-03 07:13:11⌛ | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-02-04 16:11:37 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | -0.009 |  |
| 2026-02-04 16:05:47 | Baddegama (Gin Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-02-04 15:01:05 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-02-04 16:03:00 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | -0.019 |  |
| 2026-02-04 16:03:43 | Dunamale (Aththanagalu Oya) | 0.28 | 🟢 Normal | -0.019 |  |
| 2026-02-04 16:04:28 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-02-04 15:05:16 | Thawalama (Gin Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-02-02 18:03:26⌛ | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.021 |  |
| 2026-02-04 16:04:22 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.029 |  |
| 2026-02-04 16:09:38 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.045 |  |
| 2026-02-04 16:05:29 | Weraganthota (Mahaweli Ganga) | -2.47 | 🟢 Normal | -0.046 |  |
| 2026-02-03 05:02:29⌛ | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-03 22:06:20 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.110 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)