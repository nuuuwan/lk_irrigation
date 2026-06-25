# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--26_01:08:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **189,440 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-26 01:08:05 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-26 01:06:58 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 01:06:35 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 01:06:27 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-06-26 01:05:48 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-06-26 01:03:42 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-06-26 01:03:41 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-26 01:03:32 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-06-26 01:03:32 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 01:03:18 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-26 01:02:53 | Glencourse (Kelani Ganga) | 10.00 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-26 01:02:51 | Ellagawa (Kalu Ganga) | 5.25 | 🟢 Normal | -0.011 |  |
| 2026-06-26 01:02:24 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | -0.010 |  |
| 2026-06-26 01:02:24 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-26 01:02:24 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-06-26 01:02:08 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 01:02:00 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-06-26 01:01:48 | Peradeniya (Mahaweli Ganga) | 2.46 | 🟢 Normal | -0.173 |  |
| 2026-06-26 01:01:43 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-26 01:01:41 | Hanwella (Kelani Ganga) | 1.77 | 🟢 Normal | -0.033 |  |
| 2026-06-26 01:01:39 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 01:01:11 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 01:01:08 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-06-26 01:01:02 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 01:00:51 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-26 01:00:17 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-26 01:05:48 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-06-26 00:03:42 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-26 00:04:51 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-26 01:03:42 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-06-26 01:02:53 | Glencourse (Kelani Ganga) | 10.00 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-26 01:00:51 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-26 01:03:18 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-26 01:03:32 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 01:01:11 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 01:01:02 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 01:01:39 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 01:00:17 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-06-26 00:02:18 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-26 01:02:24 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-26 00:02:26 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-25 22:07:55 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-06-26 01:03:32 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-06-26 01:08:05 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-26 01:03:41 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-26 01:06:35 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 01:06:58 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 01:02:08 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-25 18:02:21 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-26 01:06:27 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-06-25 23:08:43 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-06-26 01:01:08 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-06-25 18:01:28 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | -0.010 |  |
| 2026-06-26 00:04:55 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-06-25 18:02:25 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-06-26 01:02:00 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-06-26 00:05:05 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.010 |  |
| 2026-06-26 01:02:24 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | -0.010 |  |
| 2026-06-26 01:02:51 | Ellagawa (Kalu Ganga) | 5.25 | 🟢 Normal | -0.011 |  |
| 2026-06-26 00:01:43 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.012 |  |
| 2026-06-26 01:02:24 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-06-26 00:02:42 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | -0.021 |  |
| 2026-06-25 20:05:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.02 | 🟢 Normal | -0.024 |  |
| 2026-06-26 01:01:41 | Hanwella (Kelani Ganga) | 1.77 | 🟢 Normal | -0.033 |  |
| 2026-06-26 01:01:48 | Peradeniya (Mahaweli Ganga) | 2.46 | 🟢 Normal | -0.173 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)