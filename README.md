# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--10_20:25:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **69,545 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-10 20:25:16 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | -0.008 |  |
| 2026-02-10 20:14:47 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:13:49 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:12:52 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:09:49 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.009 |  |
| 2026-02-10 20:09:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-02-10 20:09:06 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:08:07 | Glencourse (Kelani Ganga) | 8.22 | 🟢 Normal | -0.013 |  |
| 2026-02-10 20:07:52 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:06:52 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-10 20:06:39 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:06:31 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-02-10 20:06:06 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:05:41 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.049 |  |
| 2026-02-10 20:05:35 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:04:47 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:04:26 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.021 |  |
| 2026-02-10 20:04:10 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.058 |  |
| 2026-02-10 20:03:56 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-02-10 20:03:43 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | -0.111 |  |
| 2026-02-10 20:03:41 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:03:36 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:03:29 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:03:10 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:02:51 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:02:25 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:02:20 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-10 20:02:15 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:02:03 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | -0.020 |  |
| 2026-02-10 20:01:32 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-02-10 20:01:26 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-10 20:01:25 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-02-10 20:01:10 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:01:09 | Manampitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-10 20:01:32 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-02-10 18:04:12 | Weraganthota (Mahaweli Ganga) | -2.73 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-10 20:02:20 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-10 20:06:52 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-10 20:01:26 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-10 20:13:49 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:14:47 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:04:47 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:02:15 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:06:39 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-10 18:03:04 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:12:52 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:02:51 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:03:29 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:03:10 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:03:41 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:01:10 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:02:25 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:03:36 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:06:06 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:01:09 | Manampitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:09:06 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:07:52 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-02-10 19:04:25 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:05:35 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:25:16 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | -0.008 |  |
| 2026-02-10 20:09:49 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.009 |  |
| 2026-02-10 20:03:56 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-02-10 20:01:25 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-02-10 18:01:05 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-02-10 20:06:31 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-02-10 20:08:07 | Glencourse (Kelani Ganga) | 8.22 | 🟢 Normal | -0.013 |  |
| 2026-02-10 20:02:03 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | -0.020 |  |
| 2026-02-10 20:09:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-02-10 20:04:26 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.021 |  |
| 2026-02-10 20:05:41 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.049 |  |
| 2026-02-10 20:04:10 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.058 |  |
| 2026-02-10 20:03:43 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | -0.111 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)