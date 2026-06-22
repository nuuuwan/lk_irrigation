# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--22_07:06:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **186,053 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-22 07:06:13 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-06-22 07:06:08 | Baddegama (Gin Ganga) | 1.43 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-22 07:05:53 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-22 07:05:49 | Hanwella (Kelani Ganga) | 1.97 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-22 07:05:22 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-06-22 07:05:14 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-22 07:05:06 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-22 07:04:53 | Glencourse (Kelani Ganga) | 10.20 | 🟢 Normal | 0.000 |  |
| 2026-06-22 07:04:17 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-06-22 07:04:14 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-22 07:04:10 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-06-22 07:03:57 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-22 07:03:55 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-06-22 07:03:39 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 07:03:29 | Ellagawa (Kalu Ganga) | 5.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-22 07:03:03 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 07:02:16 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-06-22 07:02:08 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 07:02:07 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 07:02:05 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-22 07:02:00 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-22 07:01:51 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-06-22 07:01:16 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.070 |  |
| 2026-06-22 07:01:15 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-22 07:00:52 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-22 07:00:07 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-22 06:43:37 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-22 06:28:37 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-06-22 06:17:07 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.052 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-22 06:13:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | 0.524 | 🔺 Rising |
| 2026-06-22 06:04:14 | Dunamale (Aththanagalu Oya) | 1.54 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-06-22 07:04:10 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-06-22 07:04:17 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-06-22 07:05:22 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-06-22 07:06:08 | Baddegama (Gin Ganga) | 1.43 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-22 07:06:13 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-06-22 06:17:07 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-22 07:05:53 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-22 07:05:49 | Hanwella (Kelani Ganga) | 1.97 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-22 07:02:05 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-22 07:03:29 | Ellagawa (Kalu Ganga) | 5.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-22 06:01:22 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-22 07:03:03 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 07:02:07 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 07:02:08 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 07:03:39 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 06:28:37 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-06-22 07:05:14 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-22 07:01:15 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-22 07:00:52 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-22 07:05:06 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-22 06:11:10 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-22 07:04:14 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-22 07:02:00 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-22 07:04:53 | Glencourse (Kelani Ganga) | 10.20 | 🟢 Normal | 0.000 |  |
| 2026-06-22 07:00:07 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-22 06:02:52 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-22 06:02:47 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-22 07:03:57 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-22 06:10:35 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-22 07:02:16 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:01:51 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-22 07:03:55 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-06-22 07:01:51 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-06-21 18:01:51 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-06-22 06:09:39 | Rathnapura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.029 |  |
| 2026-06-22 07:01:16 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.070 |  |
| 2026-06-22 06:06:03 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.185 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)