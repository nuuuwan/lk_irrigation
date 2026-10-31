# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--31_10:24:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **302,888 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 10:24:08 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | -0.007 |  |
| 2026-10-31 10:13:30 | Baddegama (Gin Ganga) | 2.63 | 🟢 Normal | -0.035 |  |
| 2026-10-31 10:12:57 | Thalgahagoda (Nilwala Ganga) | 1.66 | 🟡 Alert | -0.017 |  |
| 2026-10-31 10:10:42 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-31 10:10:23 | Dunamale (Aththanagalu Oya) | 1.97 | 🟢 Normal | -0.009 |  |
| 2026-10-31 10:09:48 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.027 |  |
| 2026-10-31 10:09:14 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.055 |  |
| 2026-10-31 10:07:36 | Rathnapura (Kalu Ganga) | 2.22 | 🟢 Normal | -0.058 |  |
| 2026-10-31 10:07:20 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-31 10:07:13 | Padiyathalawa (Maduru Oya) | 0.50 | 🟢 Normal | -0.036 |  |
| 2026-10-31 10:06:57 | Panadugama (Nilwala Ganga) | 4.78 | 🟢 Normal | -0.028 |  |
| 2026-10-31 10:06:45 | Putupaula (Kalu Ganga) | 2.42 | 🟢 Normal | -0.074 |  |
| 2026-10-31 10:05:48 | Glencourse (Kelani Ganga) | 10.63 | 🟢 Normal | 0.000 |  |
| 2026-10-31 10:05:46 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | -0.028 |  |
| 2026-10-31 10:04:49 | Galgamuwa (Mee Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-10-31 10:04:46 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.010 |  |
| 2026-10-31 10:04:09 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -0.031 |  |
| 2026-10-31 10:04:01 | Ellagawa (Kalu Ganga) | 6.80 | 🟢 Normal | -0.105 |  |
| 2026-10-31 10:03:37 | Urawa (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-31 10:03:26 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-31 10:03:24 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-10-31 10:03:07 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | -0.203 |  |
| 2026-10-31 10:03:02 | Hanwella (Kelani Ganga) | 2.66 | 🟢 Normal | -0.020 |  |
| 2026-10-31 10:02:52 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-31 10:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.16 | 🟡 Alert | -0.080 |  |
| 2026-10-31 10:02:45 | Pitabeddara (Nilwala Ganga) | 1.49 | 🟢 Normal | -0.011 |  |
| 2026-10-31 10:02:41 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | -0.022 |  |
| 2026-10-31 10:02:38 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-31 10:02:29 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-31 10:02:02 | Moragaswewa (Deduru Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-31 10:01:37 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.040 |  |
| 2026-10-31 10:01:22 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.020 |  |
| 2026-10-31 10:01:04 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-31 10:00:59 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-31 10:00:37 | Horowpothana (Yan Oya) | 2.11 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-31 10:00:37 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-10-31 10:00:36 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-31 10:00:26 | Magura (Kalu Ganga) | 2.22 | 🟢 Normal | -0.082 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 10:12:57 | Thalgahagoda (Nilwala Ganga) | 1.66 | 🟡 Alert | -0.017 |  |
| 2026-10-31 10:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.16 | 🟡 Alert | -0.080 |  |
| 2026-10-31 10:00:37 | Horowpothana (Yan Oya) | 2.11 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-31 10:02:29 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-31 10:00:36 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-31 10:02:02 | Moragaswewa (Deduru Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-31 09:00:09 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 10:04:49 | Galgamuwa (Mee Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-10-31 10:02:38 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-31 10:01:04 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-31 10:05:48 | Glencourse (Kelani Ganga) | 10.63 | 🟢 Normal | 0.000 |  |
| 2026-10-31 10:02:52 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-31 10:03:26 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-31 10:00:59 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-31 10:10:42 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-31 10:03:37 | Urawa (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-31 10:07:20 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-31 10:24:08 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | -0.007 |  |
| 2026-10-31 10:10:23 | Dunamale (Aththanagalu Oya) | 1.97 | 🟢 Normal | -0.009 |  |
| 2026-10-31 10:03:24 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-10-31 10:04:46 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.010 |  |
| 2026-10-31 10:00:37 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-10-31 10:02:45 | Pitabeddara (Nilwala Ganga) | 1.49 | 🟢 Normal | -0.011 |  |
| 2026-10-31 10:03:02 | Hanwella (Kelani Ganga) | 2.66 | 🟢 Normal | -0.020 |  |
| 2026-10-31 10:01:22 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.020 |  |
| 2026-10-31 10:02:41 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | -0.022 |  |
| 2026-10-31 10:09:48 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.027 |  |
| 2026-10-31 10:06:57 | Panadugama (Nilwala Ganga) | 4.78 | 🟢 Normal | -0.028 |  |
| 2026-10-31 10:05:46 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | -0.028 |  |
| 2026-10-31 10:04:09 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -0.031 |  |
| 2026-10-31 10:13:30 | Baddegama (Gin Ganga) | 2.63 | 🟢 Normal | -0.035 |  |
| 2026-10-31 10:07:13 | Padiyathalawa (Maduru Oya) | 0.50 | 🟢 Normal | -0.036 |  |
| 2026-10-31 10:01:37 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.040 |  |
| 2026-10-31 10:09:14 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.055 |  |
| 2026-10-31 10:07:36 | Rathnapura (Kalu Ganga) | 2.22 | 🟢 Normal | -0.058 |  |
| 2026-10-31 10:06:45 | Putupaula (Kalu Ganga) | 2.42 | 🟢 Normal | -0.074 |  |
| 2026-10-31 10:00:26 | Magura (Kalu Ganga) | 2.22 | 🟢 Normal | -0.082 |  |
| 2026-10-31 10:04:01 | Ellagawa (Kalu Ganga) | 6.80 | 🟢 Normal | -0.105 |  |
| 2026-10-31 10:03:07 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | -0.203 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)