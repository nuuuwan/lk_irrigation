# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--22_10:25:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **79,885 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 10:25:29 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-22 10:17:40 | Thalgahagoda (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-02-22 10:15:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.92 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-02-22 10:11:16 | Baddegama (Gin Ganga) | 2.62 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-22 10:11:03 | Dunamale (Aththanagalu Oya) | 1.34 | 🟢 Normal | -0.061 |  |
| 2026-02-22 10:06:59 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | -0.019 |  |
| 2026-02-22 10:06:45 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | -0.130 |  |
| 2026-02-22 10:06:43 | Thawalama (Gin Ganga) | 2.83 | 🟢 Normal | -0.075 |  |
| 2026-02-22 10:06:42 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.057 |  |
| 2026-02-22 10:06:37 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | 0.589 | 🔺 Rising |
| 2026-02-22 10:05:53 | Rathnapura (Kalu Ganga) | 4.10 | 🟢 Normal | -0.175 |  |
| 2026-02-22 10:05:50 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | -0.089 |  |
| 2026-02-22 10:05:15 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-22 10:05:04 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 10:04:26 | Magura (Kalu Ganga) | 3.40 | 🟢 Normal | -0.141 |  |
| 2026-02-22 10:04:15 | Padiyathalawa (Maduru Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-02-22 10:03:49 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 10:03:31 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-22 10:03:23 | Panadugama (Nilwala Ganga) | 4.43 | 🟢 Normal | -0.056 |  |
| 2026-02-22 10:03:18 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-02-22 10:03:00 | Hanwella (Kelani Ganga) | 2.79 | 🟢 Normal | -0.091 |  |
| 2026-02-22 10:02:56 | Urawa (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.773 |  |
| 2026-02-22 10:02:54 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-22 10:02:52 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.061 |  |
| 2026-02-22 10:02:48 | Glencourse (Kelani Ganga) | 10.50 | 🟢 Normal | -0.160 |  |
| 2026-02-22 10:02:35 | Giriulla (Maha Oya) | 2.16 | 🟢 Normal | -0.192 |  |
| 2026-02-22 10:02:33 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-02-22 10:02:31 | Putupaula (Kalu Ganga) | 1.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-22 10:02:21 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.021 |  |
| 2026-02-22 10:01:56 | Wellawaya (Kirindi Oya) | 1.39 | 🟢 Normal | -56.903 |  |
| 2026-02-22 10:01:48 | Thanamalwila (Kirindi Oya) | 1.72 | 🟢 Normal | -0.066 |  |
| 2026-02-22 10:01:47 | Pitabeddara (Nilwala Ganga) | 1.71 | 🟢 Normal | -0.305 |  |
| 2026-02-22 10:01:34 | Nakkala (Kumbukkan Oya) | 1.47 | 🟢 Normal | -0.030 |  |
| 2026-02-22 10:01:20 | Manampitiya (Mahaweli Ganga) | 4.38 | 🟠 Minor Flood | -0.050 |  |
| 2026-02-22 10:01:13 | Ellagawa (Kalu Ganga) | 7.70 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-02-22 10:01:11 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-02-22 10:01:02 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-22 10:00:54 | Wellawaya (Kirindi Oya) | 2.37 | 🟢 Normal | -56.903 |  |
| 2026-02-22 10:00:50 | Horowpothana (Yan Oya) | 1.95 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-02-22 10:00:10 | Weraganthota (Mahaweli Ganga) | -0.96 | 🟢 Normal | -0.080 |  |
| 2026-02-22 09:59:03 | Urawa (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.773 |  |
| 2026-02-22 09:52:20 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.089 |  |
| 2026-02-22 09:52:19 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.089 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 10:01:20 | Manampitiya (Mahaweli Ganga) | 4.38 | 🟠 Minor Flood | -0.050 |  |
| 2026-02-22 10:06:37 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | 0.589 | 🔺 Rising |
| 2026-02-22 10:00:50 | Horowpothana (Yan Oya) | 1.95 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-02-22 10:15:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.92 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-02-22 10:01:13 | Ellagawa (Kalu Ganga) | 7.70 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-02-22 10:02:33 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-02-22 10:11:16 | Baddegama (Gin Ganga) | 2.62 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-22 10:01:11 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-02-22 10:17:40 | Thalgahagoda (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-02-22 10:02:31 | Putupaula (Kalu Ganga) | 1.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-22 10:01:02 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-22 10:03:31 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-22 10:25:29 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-22 10:03:49 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 10:05:15 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-22 10:05:04 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 10:03:18 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-02-22 10:04:15 | Padiyathalawa (Maduru Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-02-22 09:01:02 | Kuda Oya (Kirindi Oya) | 2.41 | 🟢 Normal | -0.011 |  |
| 2026-02-22 10:06:59 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | -0.019 |  |
| 2026-02-22 10:02:21 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.021 |  |
| 2026-02-22 10:01:34 | Nakkala (Kumbukkan Oya) | 1.47 | 🟢 Normal | -0.030 |  |
| 2026-02-22 10:03:23 | Panadugama (Nilwala Ganga) | 4.43 | 🟢 Normal | -0.056 |  |
| 2026-02-22 10:06:42 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.057 |  |
| 2026-02-22 10:02:52 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.061 |  |
| 2026-02-22 10:11:03 | Dunamale (Aththanagalu Oya) | 1.34 | 🟢 Normal | -0.061 |  |
| 2026-02-22 10:01:48 | Thanamalwila (Kirindi Oya) | 1.72 | 🟢 Normal | -0.066 |  |
| 2026-02-22 10:06:43 | Thawalama (Gin Ganga) | 2.83 | 🟢 Normal | -0.075 |  |
| 2026-02-22 10:00:10 | Weraganthota (Mahaweli Ganga) | -0.96 | 🟢 Normal | -0.080 |  |
| 2026-02-22 10:05:50 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | -0.089 |  |
| 2026-02-22 10:03:00 | Hanwella (Kelani Ganga) | 2.79 | 🟢 Normal | -0.091 |  |
| 2026-02-22 10:06:45 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | -0.130 |  |
| 2026-02-22 10:04:26 | Magura (Kalu Ganga) | 3.40 | 🟢 Normal | -0.141 |  |
| 2026-02-22 10:02:48 | Glencourse (Kelani Ganga) | 10.50 | 🟢 Normal | -0.160 |  |
| 2026-02-22 10:05:53 | Rathnapura (Kalu Ganga) | 4.10 | 🟢 Normal | -0.175 |  |
| 2026-02-22 10:02:35 | Giriulla (Maha Oya) | 2.16 | 🟢 Normal | -0.192 |  |
| 2026-02-22 10:01:47 | Pitabeddara (Nilwala Ganga) | 1.71 | 🟢 Normal | -0.305 |  |
| 2026-02-22 10:02:56 | Urawa (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.773 |  |
| 2026-02-22 10:01:56 | Wellawaya (Kirindi Oya) | 1.39 | 🟢 Normal | -56.903 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)