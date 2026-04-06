# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_21:00:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **118,014 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **12** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 21:00:24 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-06 21:00:12 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-06 20:38:07 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-04-06 20:17:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | -0.022 |  |
| 2026-04-06 20:10:26 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | -0.229 |  |
| 2026-04-06 20:10:10 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-06 20:09:39 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-06 20:08:24 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-06 20:07:38 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-06 20:07:15 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.050 |  |
| 2026-04-06 20:07:03 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-06 20:07:01 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 20:01:32 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-04-06 20:00:53 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-04-06 20:00:59 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-06 20:01:29 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-06 21:00:12 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-06 20:02:14 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-06 20:07:38 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-06 20:06:01 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-06 20:01:43 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-06 20:38:07 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-04-06 20:04:23 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-06 20:05:44 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-06 20:01:06 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-06 20:01:51 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-06 20:01:32 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:00:26 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-06 20:06:31 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-06 20:02:36 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 20:02:12 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-06 20:05:43 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-04-06 19:08:37 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-04-06 20:07:03 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-06 20:04:43 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-06 20:08:24 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-06 20:03:23 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-04-06 20:10:10 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-06 20:09:39 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:01:18 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-04-06 20:01:18 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-04-06 21:00:24 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-06 20:07:01 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.011 |  |
| 2026-04-06 20:02:26 | Magura (Kalu Ganga) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-04-06 20:17:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | -0.022 |  |
| 2026-04-06 20:04:01 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.029 |  |
| 2026-04-06 20:07:15 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.050 |  |
| 2026-04-06 18:01:26 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.079 |  |
| 2026-04-06 19:03:52 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | -0.088 |  |
| 2026-04-06 20:01:26 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.093 |  |
| 2026-04-06 20:10:26 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | -0.229 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)