# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--10_13:03:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **41,790 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 13:03:30 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:03:25 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 13:03:14 | Katharagama (Menik Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:03:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.33 | 🟢 Normal | -0.030 |  |
| 2026-01-10 13:02:14 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:02:13 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:02:08 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:01:51 | Yaka Wewa (Ma Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:01:27 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:01:23 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-01-10 13:01:22 | Weraganthota (Mahaweli Ganga) | -1.29 | 🟢 Normal | -0.020 |  |
| 2026-01-10 13:01:16 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:01:14 | Ellagawa (Kalu Ganga) | 4.06 | 🟢 Normal | -0.010 |  |
| 2026-01-10 13:00:43 | Horowpothana (Yan Oya) | 2.73 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:00:34 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:00:29 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-10 12:20:50 | Katharagama (Menik Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-10 12:16:47 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.057 |  |
| 2026-01-10 12:11:11 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | -0.009 |  |
| 2026-01-10 12:08:26 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-10 12:08:24 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-10 12:08:02 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-10 12:07:38 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-10 12:07:19 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-10 12:06:39 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-10 12:06:24 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.029 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 13:01:23 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-01-10 12:00:58 | Thanthirimale (Malwathu Oya) | 1.88 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-10 13:03:25 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 13:02:08 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:01:16 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:02:14 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:01:51 | Yaka Wewa (Ma Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-10 12:03:37 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:00:43 | Horowpothana (Yan Oya) | 2.73 | 🟢 Normal | 0.000 |  |
| 2026-01-10 12:07:38 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-10 12:03:38 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-10 12:02:34 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:03:30 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-10 12:06:39 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:00:29 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:01:27 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-10 12:07:19 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:03:14 | Katharagama (Menik Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-10 12:05:29 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-10 12:08:26 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:00:34 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:02:13 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-10 12:04:53 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-10 12:08:02 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-10 12:11:11 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | -0.009 |  |
| 2026-01-10 13:01:14 | Ellagawa (Kalu Ganga) | 4.06 | 🟢 Normal | -0.010 |  |
| 2026-01-10 13:01:22 | Weraganthota (Mahaweli Ganga) | -1.29 | 🟢 Normal | -0.020 |  |
| 2026-01-10 12:02:18 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-01-10 12:02:56 | Baddegama (Gin Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-01-10 12:03:45 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-01-10 12:03:24 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.021 |  |
| 2026-01-10 12:06:24 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.029 |  |
| 2026-01-10 13:03:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.33 | 🟢 Normal | -0.030 |  |
| 2026-01-10 12:02:59 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.040 |  |
| 2026-01-10 12:16:47 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.057 |  |
| 2026-01-10 12:01:10 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.072 |  |
| 2026-01-10 12:02:32 | Putupaula (Kalu Ganga) | 0.33 | 🟢 Normal | -0.084 |  |
| 2026-01-10 12:01:21 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.132 |  |
| 2026-01-10 12:05:49 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)