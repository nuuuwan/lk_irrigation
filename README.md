# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--17_18:07:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **182,031 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-17 18:07:19 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-17 18:06:57 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-17 18:06:48 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-06-17 18:06:30 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-17 18:05:46 | Nawalapitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | 0.277 | 🔺 Rising |
| 2026-06-17 18:05:40 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-06-17 18:05:17 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-06-17 18:05:14 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.009 |  |
| 2026-06-17 18:04:43 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-17 18:04:23 | Rathnapura (Kalu Ganga) | 2.49 | 🟢 Normal | 0.662 | 🔺 Rising |
| 2026-06-17 18:04:11 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-17 18:04:01 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-17 18:04:00 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-17 18:03:42 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-17 18:03:40 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-17 18:03:20 | Hanwella (Kelani Ganga) | 1.87 | 🟢 Normal | -0.020 |  |
| 2026-06-17 18:03:17 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.090 |  |
| 2026-06-17 18:03:14 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-17 18:03:11 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.052 |  |
| 2026-06-17 18:03:02 | Ellagawa (Kalu Ganga) | 5.31 | 🟢 Normal | -0.010 |  |
| 2026-06-17 18:02:56 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | 0.000 |  |
| 2026-06-17 18:02:29 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-06-17 18:02:25 | Magura (Kalu Ganga) | 1.88 | 🟢 Normal | -0.011 |  |
| 2026-06-17 18:02:23 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-06-17 18:02:16 | Deraniyagala (Kelani Ganga) | 2.72 | 🟢 Normal | 0.705 | 🔺 Rising |
| 2026-06-17 18:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-17 18:02:08 | Glencourse (Kelani Ganga) | 9.95 | 🟢 Normal | -0.022 |  |
| 2026-06-17 18:01:53 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-17 18:01:33 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-06-17 18:01:30 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | -0.127 |  |
| 2026-06-17 18:01:29 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-06-17 18:01:25 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-06-17 18:01:14 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-17 18:00:54 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-17 18:00:47 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-06-17 18:00:23 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-17 18:00:20 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-17 18:00:10 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | -0.021 |  |
| 2026-06-17 17:30:40 | Panadugama (Nilwala Ganga) | 2.82 | 🟢 Normal | 0.033 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-17 18:02:16 | Deraniyagala (Kelani Ganga) | 2.72 | 🟢 Normal | 0.705 | 🔺 Rising |
| 2026-06-17 18:04:23 | Rathnapura (Kalu Ganga) | 2.49 | 🟢 Normal | 0.662 | 🔺 Rising |
| 2026-06-17 18:05:46 | Nawalapitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | 0.277 | 🔺 Rising |
| 2026-06-17 17:08:40 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-06-17 18:03:14 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-17 18:06:57 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-17 18:06:30 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-17 18:07:19 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-17 18:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-17 18:04:43 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-17 18:02:56 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | 0.000 |  |
| 2026-06-17 18:01:14 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-17 18:00:23 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-17 18:00:54 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-17 18:04:11 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-17 18:01:33 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-06-17 18:04:01 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-17 18:00:20 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-17 18:04:00 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-17 18:05:40 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-06-17 18:03:42 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-17 18:01:53 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-17 18:06:48 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-06-17 18:03:40 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-17 18:05:14 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.009 |  |
| 2026-06-17 18:03:02 | Ellagawa (Kalu Ganga) | 5.31 | 🟢 Normal | -0.010 |  |
| 2026-06-17 18:02:23 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-06-17 18:05:17 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-06-17 18:02:29 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-06-17 18:01:25 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-06-17 18:00:47 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-06-17 18:01:29 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-06-17 18:02:25 | Magura (Kalu Ganga) | 1.88 | 🟢 Normal | -0.011 |  |
| 2026-06-17 18:03:20 | Hanwella (Kelani Ganga) | 1.87 | 🟢 Normal | -0.020 |  |
| 2026-06-17 18:00:10 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | -0.021 |  |
| 2026-06-17 18:02:08 | Glencourse (Kelani Ganga) | 9.95 | 🟢 Normal | -0.022 |  |
| 2026-06-17 18:03:11 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.052 |  |
| 2026-06-17 18:03:17 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.090 |  |
| 2026-06-17 18:01:30 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | -0.127 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)