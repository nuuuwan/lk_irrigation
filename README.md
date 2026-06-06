# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--06_10:22:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **171,916 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 10:22:22 | Putupaula (Kalu Ganga) | 1.61 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-06-06 10:19:18 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-06-06 10:13:33 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-06-06 10:11:19 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-06 10:09:10 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-06 10:07:42 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.019 |  |
| 2026-06-06 10:07:35 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-06 10:07:25 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-06-06 10:07:23 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-06-06 10:07:21 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-06 10:07:02 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.105 |  |
| 2026-06-06 10:06:27 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | -0.029 |  |
| 2026-06-06 10:06:20 | Rathnapura (Kalu Ganga) | 3.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 10:06:02 | Baddegama (Gin Ganga) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-06-06 10:05:36 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-06-06 10:04:18 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-06-06 10:04:13 | Nawalapitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-06 10:04:07 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | -0.030 |  |
| 2026-06-06 10:03:59 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-06 10:03:52 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-06 10:03:25 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-06 10:03:14 | Hanwella (Kelani Ganga) | 3.66 | 🟢 Normal | -0.030 |  |
| 2026-06-06 10:02:57 | Giriulla (Maha Oya) | 1.74 | 🟢 Normal | -0.020 |  |
| 2026-06-06 10:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 10:02:48 | Deraniyagala (Kelani Ganga) | 1.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-06 10:02:33 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-06 10:02:31 | Glencourse (Kelani Ganga) | 11.43 | 🟢 Normal | -0.071 |  |
| 2026-06-06 10:02:25 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-06 10:02:23 | Dunamale (Aththanagalu Oya) | 3.29 | 🟢 Normal | -0.027 |  |
| 2026-06-06 10:02:17 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-06 10:02:02 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-06 10:01:42 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.040 |  |
| 2026-06-06 10:01:23 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-06-06 10:01:12 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-06 10:01:07 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-06-06 10:01:06 | Ellagawa (Kalu Ganga) | 7.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-06 10:00:49 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-06 10:00:48 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-06 10:00:12 | Nagalagam Street (Kelani Ganga) | 0.44 | 🟢 Normal | -0.052 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 10:04:18 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-06-06 10:02:48 | Deraniyagala (Kelani Ganga) | 1.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-06 10:04:13 | Nawalapitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-06 10:01:06 | Ellagawa (Kalu Ganga) | 7.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-06 10:19:18 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-06-06 10:22:22 | Putupaula (Kalu Ganga) | 1.61 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-06-06 10:09:10 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-06 10:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 10:06:20 | Rathnapura (Kalu Ganga) | 3.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 10:01:12 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-06 10:00:48 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-06 10:03:59 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-06 10:02:25 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-06 10:07:21 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-06 10:02:17 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-06 10:13:33 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-06-06 10:11:19 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-06 10:03:52 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-06 10:02:33 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-06 10:07:35 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-06 10:02:02 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-06 10:05:36 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-06-06 10:00:49 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-06 10:07:23 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-06-06 10:03:25 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-06 10:06:02 | Baddegama (Gin Ganga) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-06-06 10:01:23 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-06-06 10:01:07 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-06-06 10:07:42 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.019 |  |
| 2026-06-06 10:07:25 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-06-06 10:02:57 | Giriulla (Maha Oya) | 1.74 | 🟢 Normal | -0.020 |  |
| 2026-06-06 10:02:23 | Dunamale (Aththanagalu Oya) | 3.29 | 🟢 Normal | -0.027 |  |
| 2026-06-06 10:06:27 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | -0.029 |  |
| 2026-06-06 10:04:07 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | -0.030 |  |
| 2026-06-06 10:03:14 | Hanwella (Kelani Ganga) | 3.66 | 🟢 Normal | -0.030 |  |
| 2026-06-06 10:01:42 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.040 |  |
| 2026-06-06 10:00:12 | Nagalagam Street (Kelani Ganga) | 0.44 | 🟢 Normal | -0.052 |  |
| 2026-06-06 10:02:31 | Glencourse (Kelani Ganga) | 11.43 | 🟢 Normal | -0.071 |  |
| 2026-06-06 10:07:02 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.105 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)