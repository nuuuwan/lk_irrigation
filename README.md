# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--21_16:11:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **158,002 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-21 16:11:49 | Dunamale (Aththanagalu Oya) | 1.80 | 🟢 Normal | -0.017 |  |
| 2026-05-21 16:11:26 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:10:02 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:10:00 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:09:25 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:08:49 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | 0.005 |  |
| 2026-05-21 16:07:33 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:07:29 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-21 16:06:42 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.019 |  |
| 2026-05-21 16:06:35 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:06:22 | Galgamuwa (Mee Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:06:15 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:05:46 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:05:25 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.019 |  |
| 2026-05-21 16:04:53 | Glencourse (Kelani Ganga) | 9.72 | 🟢 Normal | -0.049 |  |
| 2026-05-21 16:04:50 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | -0.021 |  |
| 2026-05-21 16:04:36 | Moragaswewa (Deduru Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:03:44 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:03:36 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-21 16:03:14 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -0.020 |  |
| 2026-05-21 16:03:14 | Ellagawa (Kalu Ganga) | 5.49 | 🟢 Normal | -0.020 |  |
| 2026-05-21 16:03:10 | Hanwella (Kelani Ganga) | 1.72 | 🟢 Normal | -0.020 |  |
| 2026-05-21 16:03:01 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:02:56 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-21 16:02:42 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.042 |  |
| 2026-05-21 16:02:39 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-21 16:02:25 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:02:17 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-21 16:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.99 | 🟢 Normal | -0.010 |  |
| 2026-05-21 16:02:03 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:01:54 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-05-21 16:01:41 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:01:38 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:01:36 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.123 |  |
| 2026-05-21 16:01:34 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-05-21 16:01:07 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:00:50 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:00:42 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:00:25 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-21 15:29:54 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-21 16:02:39 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-21 15:17:24 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-05-21 16:03:36 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-21 16:07:29 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-21 16:02:56 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-21 16:02:17 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-21 16:08:49 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | 0.005 |  |
| 2026-05-21 16:06:15 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:10:02 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:04:36 | Moragaswewa (Deduru Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:03:44 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:07:33 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:06:22 | Galgamuwa (Mee Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:06:35 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:11:26 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:03:01 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-21 15:29:54 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:02:03 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:01:38 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:01:41 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:01:07 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:02:25 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:05:46 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:00:42 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:10:00 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:09:25 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:01:54 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-05-21 16:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.99 | 🟢 Normal | -0.010 |  |
| 2026-05-21 16:01:34 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-05-21 16:11:49 | Dunamale (Aththanagalu Oya) | 1.80 | 🟢 Normal | -0.017 |  |
| 2026-05-21 16:06:42 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.019 |  |
| 2026-05-21 16:05:25 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.019 |  |
| 2026-05-21 16:03:14 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -0.020 |  |
| 2026-05-21 16:03:14 | Ellagawa (Kalu Ganga) | 5.49 | 🟢 Normal | -0.020 |  |
| 2026-05-21 16:03:10 | Hanwella (Kelani Ganga) | 1.72 | 🟢 Normal | -0.020 |  |
| 2026-05-21 16:04:50 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | -0.021 |  |
| 2026-05-21 16:02:42 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.042 |  |
| 2026-05-21 16:04:53 | Glencourse (Kelani Ganga) | 9.72 | 🟢 Normal | -0.049 |  |
| 2026-05-21 16:01:36 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.123 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)